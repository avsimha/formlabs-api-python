import sys
import pathlib
import requests
import time
import json
import formlabs_local_api_minimal as formlabs

# Set the path to PreFormServer
if sys.platform == 'win32':
    pathToPreformServer = pathlib.Path("C:\\Users\\avsimha\\PreFormServer\\PreFormServer.exe")
else:
    print("Unsupported platform")
    sys.exit(1)

BASE_URL = "http://localhost:44388"

class PreFormApi:
    @staticmethod
    def discover_devices(timeout_seconds=10):
        data = {"timeout_seconds": timeout_seconds}
        try:
            response = requests.post(f"{BASE_URL}/discover-devices/", json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error discovering devices: {e}")
            return None

    @staticmethod
    def get_device_details(device_id):
        try:
            response = requests.get(f"{BASE_URL}/devices/{device_id}/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting device details: {e}")
            return None

    @staticmethod
    def get_scene():
        try:
            response = requests.get(f"{BASE_URL}/scene/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting scene information: {e}")
            return None

    @staticmethod
    def get_print_validation():
        try:
            response = requests.get(f"{BASE_URL}/scene/print-validation/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting print validation: {e}")
            return None

def print_device_info(device):
    print(f"Device ID: {device['id']}")
    print(f"Product Name: {device['product_name']}")
    print(f"Status: {device['status']}")
    print(f"Connection Type: {device['connection_type']}")
    if 'ip_address' in device:
        print(f"IP Address: {device['ip_address']}")
    print(f"Firmware Version: {device['firmware_version']}")
    if 'is_remote_print_enabled' in device:
        print(f"Remote Print Enabled: {device['is_remote_print_enabled']}")
    if 'tank_material_code' in device:
        print(f"Tank Material: {device['tank_material_code']}")
    print("-" * 40)

def is_real_printer(device):
    return device['connection_type'] != "VIRTUAL"

def select_printer(real_devices):
    print("\nAvailable printers:")
    for i, device in enumerate(real_devices):
        print(f"{i + 1}. {device['product_name']} (ID: {device['id']})")
    
    while True:
        try:
            selection = int(input("\nEnter the number of the printer you want to select: ")) - 1
            if 0 <= selection < len(real_devices):
                return real_devices[selection]
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def select_info_type():
    print("\nSelect the type of information you want to dump:")
    print("1. Printer Details")
    print("2. Current Scene")
    print("3. Print Validation")
    print("4. All of the above")

    while True:
        try:
            selection = int(input("\nEnter your choice (1-4): "))
            if 1 <= selection <= 4:
                return selection
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def print_json(title, data):
    print(f"\n{title}:")
    print(json.dumps(data, indent=2))
    print("\n" + "=" * 80 + "\n")

def main():
    print("Starting PreFormServer...")
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer):
        print("PreFormServer started successfully.")
        
        api = PreFormApi()

        print("Scanning for printers...")
        discovered_devices = api.discover_devices()

        if discovered_devices and discovered_devices['count'] > 0:
            real_devices = [device for device in discovered_devices['devices'] if is_real_printer(device)]
            print(f"Found {len(real_devices)} real device(s):")
            for device in real_devices:
                device_details = api.get_device_details(device['id'])
                if device_details:
                    print_device_info(device_details)
            
            while True:
                selected_device = select_printer(real_devices)
                info_type = select_info_type()

                if info_type == 4:
                    print("\nDumping all available information:")
                    print_json("Printer Details", api.get_device_details(selected_device['id']))
                    print_json("Current Scene", api.get_scene())
                    print_json("Print Validation", api.get_print_validation())
                else:
                    if info_type == 1:
                        info = api.get_device_details(selected_device['id'])
                        title = "Full JSON dump of the selected printer"
                    elif info_type == 2:
                        info = api.get_scene()
                        title = "Full JSON dump of the current scene"
                    elif info_type == 3:
                        info = api.get_print_validation()
                        title = "Full JSON dump of the print validation"

                    print_json(title, info)

                continue_choice = input("\nDo you want to view details for another printer? (y/n): ").lower()
                if continue_choice != 'y':
                    break
        else:
            print("No devices found.")

    print("Exiting the program.")

if __name__ == "__main__":
    main()
