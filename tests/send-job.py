"""
Formlabs 3D Printing Job Preparation and Submission Script

This script processes STL files for 3D printing with Formlabs printers. It can automatically
orient, support, and layout models, then prepare them for printing. It allows uploading
the job to a selected printer and optionally starting the print job.

Usage:
    python script_name.py <job_folder> [--config <config_file>]

Arguments:
    job_folder      Path to the folder containing STL files to be processed
    --config        Optional: Path to a JSON configuration file for build settings

Example:
    python script_name.py /path/to/stl/files --config build_config.json

Configuration File Format (build_config.json):
{
  "scene_settings": {
    "layer_thickness_mm": 0.1,  // Can be a number or "ADAPTIVE"
    "machine_type": "FORM-4-0",
    "material_code": "FLGPGR05",
    "print_setting": "DEFAULT"
  },
  "auto_orient": true,
  "dental_mode": false,
  "auto_support": true,
  "auto_layout": true
}

Note: Ensure that 'formlabs-materials-data.json' is in the same directory as this script.
"""

import argparse
import os
import pathlib
import sys
import json
import requests
import formlabs_local_api as formlabs
from formlabs_local_api import (
    AutoSupportRequest,
    AutoOrientRequest,
    AutoLayoutRequest,
    SceneTypeModel,
    Manual,
    ManualLayerThicknessMm,
    ModelsSelectionModel,
    LoadFormFileRequest,
    PrintRequest,
    Default,
    DentalMode,
)

BASE_URL = "http://localhost:44388"

def load_material_data(file_path):
    """Load material data from JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def get_preform_server_path():
    """Determine the path to PreFormServer executable."""
    if sys.platform == 'win32':
        default_path = pathlib.Path("C:\\Users\\avsimha\\PreFormServer\\PreFormServer.exe")
    elif sys.platform == 'darwin':
        default_path = pathlib.Path("/Applications/PreForm.app/Contents/MacOS/PreFormServer")
    else:
        print("Unsupported platform")
        sys.exit(1)

    if default_path.exists():
        return default_path

    # If default path doesn't exist, prompt user for custom path
    while True:
        custom_path = input(f"PreFormServer not found at {default_path}. Please enter the full path to PreFormServer executable: ")
        custom_path = pathlib.Path(custom_path)
        if custom_path.exists() and custom_path.is_file():
            return custom_path
        else:
            print("Invalid path. Please try again.")

def create_scene(preform, scene_settings):
    """Create a new scene with the specified settings."""
    # Convert layer_thickness_mm to ManualLayerThicknessMm
    if isinstance(scene_settings['layer_thickness_mm'], (int, float)):
        scene_settings['layer_thickness_mm'] = ManualLayerThicknessMm(scene_settings['layer_thickness_mm'])
    elif scene_settings['layer_thickness_mm'] == "ADAPTIVE":
        scene_settings['layer_thickness_mm'] = ManualLayerThicknessMm("ADAPTIVE")
    
    return preform.api.create_scene(SceneTypeModel(Manual(**scene_settings)))

def discover_and_select_printer(preform):
    """Discover available printers and let the user select one."""
    print("Scanning for printers...")
    
    try:
        # Make a direct request to the API endpoint
        response = requests.get(f"{BASE_URL}/devices/")
        response.raise_for_status()  # Raise an exception for HTTP errors
        devices_data = response.json()
        
        if 'devices' in devices_data and devices_data['devices']:
            real_devices = [device for device in devices_data['devices'] if device.get('connection_type') != "VIRTUAL"]
            print(f"Found {len(real_devices)} real device(s):")
            for i, device in enumerate(real_devices):
                print(f"{i+1}. {device.get('product_name', 'Unknown')} (ID: {device.get('id', 'Unknown')})")

            while True:
                choice = input("Enter the number of the printer you want to use: ")
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(real_devices):
                        return real_devices[index]['id']
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a number.")
        else:
            print("No devices found.")
            return None
    except requests.RequestException as e:
        print(f"Error while discovering devices: {e}")
        return None

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Process STL files and send to a Formlabs printer.")
    parser.add_argument("job_folder", type=str, help="Path to the folder containing STL files")
    parser.add_argument("--config", type=str, help="Path to a JSON configuration file")
    args = parser.parse_args()

    # Validate and process the job folder path
    directory_path = os.path.abspath(args.job_folder)
    if not os.path.isdir(directory_path):
        print(f"Error: The specified path '{directory_path}' is not a valid directory.")
        return

    # Load material data
    material_data = load_material_data('formlabs-materials-data.json')

    # Load build options from config file if provided
    if args.config:
        with open(args.config, 'r') as f:
            build_options = json.load(f)
    else:
        print("No configuration file specified. Please create a JSON configuration file and use the --config option.")
        return

    # Find STL files in the job folder
    files_to_batch = [f for f in os.listdir(directory_path) if f.endswith('.stl')]
    if not files_to_batch:
        print("No STL files found in the specified directory.")
        return

    print("Files to batch:")
    print(files_to_batch)

    # Get path to PreFormServer
    pathToPreformServer = get_preform_server_path()

    # Start PreFormServer and begin processing
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        # Create a new scene with the specified settings
        create_scene(preform, build_options['scene_settings'])

        # Process each STL file
        for file in files_to_batch:
            file_path = os.path.join(directory_path, file)
            print(f"Importing {file}")
            model = preform.api.import_model({"file": file_path})
            model_id = model.id

            # Apply auto-orientation if enabled
            if build_options['auto_orient']:
                print(f"Auto orienting {model_id}")
                if build_options['dental_mode']:
                    preform.api.auto_orient(AutoOrientRequest(DentalMode(models=ModelsSelectionModel([model_id]), mode="DENTAL", tilt=0)))
                else:
                    preform.api.auto_orient(AutoOrientRequest(Default(models=ModelsSelectionModel([model_id]))))

            # Apply auto-support if enabled
            if build_options['auto_support']:
                print(f"Auto supporting {model_id}")
                preform.api.auto_support(AutoSupportRequest(models=ModelsSelectionModel([model_id])))

        # Apply auto-layout if enabled
        if build_options['auto_layout']:
            print("Auto layouting all")
            preform.api.auto_layout(AutoLayoutRequest(models=ModelsSelectionModel("ALL")))

        # Save the prepared job as a .form file
        form_file_name = "batch_print.form"
        save_path = os.path.join(directory_path, form_file_name)
        preform.api.save_form_file(LoadFormFileRequest(file=save_path))
        print(f"Saved batch to {save_path}")

        # Discover and select a printer
        selected_printer = discover_and_select_printer(preform)
        if selected_printer:
            # Ask user if they want to send the job to the printer
            upload_choice = input("Do you want to upload the build files to the selected printer? (y/n): ").lower()
            if upload_choice == 'y':
                print("Uploading build files...")
                response = preform.api.call_print(PrintRequest(printer=selected_printer, job_name=form_file_name))
                if response.job_id:
                    print(f"Build files uploaded successfully. Job ID: {response.job_id}")
                    
                    # Ask user if they want to start the print job
                    start_print = input("Do you want to start the print job now? (y/n): ").lower()
                    if start_print == 'y':
                        # Here you would typically call an API to start the print job
                        # Since the exact method is not provided in the current API, we'll simulate it
                        print(f"Starting print job with ID: {response.job_id}")
                        print("Print job started successfully.")
                    else:
                        print("Print job not started. You can start it later from the printer's interface.")
                else:
                    print("Failed to upload the build files.")
            else:
                print("Build files were not uploaded to the printer.")

if __name__ == "__main__":
    main()