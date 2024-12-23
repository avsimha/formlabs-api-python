import os
import pathlib
import sys
from formlabs_local_api import PreFormApi, PrintRequest
from formlabs_local_api.models import LoadFormFileRequest

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

def discover_and_select_printer(preform):
    """Discover printers and let the user select one."""
    try:
        # Fetch devices using the API method
        devices = preform.api.get_devices()

        # Filter out invalid or virtual devices
        real_devices = [
            device for device in devices if device.connection_type not in ("VIRTUAL", None)
        ]

        if not real_devices:
            print("No printers found.")
            return None

        # Display the filtered devices
        print("Available Printers:")
        for idx, device in enumerate(real_devices):
            print(f"{idx + 1}: {device.product_name} (ID: {device.id})")

        # Prompt user for selection
        while True:
            choice = input("Select a printer by number: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(real_devices):
                    return real_devices[index].id
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
    except Exception as e:
        print(f"Error discovering printers: {e}")
        return None

def upload_form_file(preform, printer_id, file_path):
    """Load a .form file and send it to the selected printer."""
    if not os.path.isfile(file_path):
        print("Invalid file path. Please check and try again.")
        return

    print(f"Uploading {file_path} to printer {printer_id}...")
    try:
        # Load the .form file into the PreFormServer
        load_request = LoadFormFileRequest(file=file_path)
        preform.api.load_form_file(load_request)

        # Send the job to the printer
        job_name = os.path.basename(file_path)
        print_request = PrintRequest(printer=printer_id, job_name=job_name)
        response = preform.api.call_print(print_request)

        if response.job_id:
            print(f"Print job uploaded successfully. Job ID: {response.job_id}")
        else:
            print("Failed to upload the print job.")
    except Exception as e:
        print(f"Error uploading the print job: {e}")

def main():
    # Get the path to the PreFormServer executable
    path_to_preform_server = get_preform_server_path()

    with PreFormApi.start_preform_server(pathToPreformServer=path_to_preform_server) as preform:
        # Discover and select a printer
        selected_printer = discover_and_select_printer(preform)
        if not selected_printer:
            print("No printer selected. Exiting.")
            return

        # Ask for the .form file path
        file_path = input("Enter the full path to the .form file: ")
        upload_form_file(preform, selected_printer, file_path)

if __name__ == "__main__":
    main()
