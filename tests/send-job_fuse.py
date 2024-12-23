"""
Formlabs 3D Printing Job Preparation and Submission Script

This script processes STL files for 3D printing with Formlabs printers. It can automatically
orient, support, and layout models, then prepare them for printing. It allows uploading
the job to a selected printer and optionally starting the print job.

Usage:
    python script_name.py <build_file> [--config <config_file>]

Arguments:
    build_file      Path to the build file that should be uploaded
    --config        Optional: Path to a JSON configuration file for build settings

Example:
    python script_name.py /path/to/build/file.form --config build-config_fuse.json

Configuration File Format (build-config_fuse.json):
{
  "scene_settings": {
    "layer_thickness_mm": 0.11,
    "machine_type": "FS30-1-0",
    "material_code": "FLP12G01",
    "print_setting": "DEFAULT_V4"
  },
  "auto_orient": true,
  "dental_mode": false,
  "auto_support": true,
  "auto_pack": true
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
    SceneTypeModel,
    Manual,
    ManualLayerThicknessMm,
    PrintRequest,
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
    parser = argparse.ArgumentParser()
    # parser.add_argument("build_file", type=str, help="Path to the Preform build file")
    parser.add_argument("--config", type=str, help="Path to a JSON configuration file")
    args = parser.parse_args()

    # Validate and process the build file path
    # build_file_path = pathlib.Path(args.build_file)
    build_file_path = "test_print.form"
    # if not build_file_path.exists() and build_file_path.is_file():
    #     print(f"Error: The specified path '{build_file_path}' is not valid.")
    #     return

    # Load material data
    material_data = load_material_data('formlabs-materials-data.json')

    # Load build options from config file if provided
    if args.config:
        with open(args.config, 'r') as f:
            build_options = json.load(f)
    else:
        print("No configuration file specified. Please create a JSON configuration file and use the --config option.")
        return
    
    # Get path to PreFormServer
    pathToPreformServer = get_preform_server_path()

    # Start PreFormServer and begin processing
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer) as preform:
        # Create a new scene with the specified settings
        create_scene(preform, build_options['scene_settings'])

        # Discover and select a printer
        selected_printer = discover_and_select_printer(preform)
        if selected_printer:
            # Ask user if they want to send the job to the printer
            upload_choice = input("Do you want to upload the build files to the selected printer? (y/n): ").lower()
            if upload_choice == 'y':
                print("Uploading build files...")
                response = preform.api.call_print(PrintRequest(printer=selected_printer, job_name=build_file_path))
                if response.job_id:
                    print(f"Build files uploaded successfully. Job ID: {response.job_id}")
                else:
                    print("Failed to upload the build files.")
            else:
                print("Build files were not uploaded to the printer.")

if __name__ == "__main__":
    main()