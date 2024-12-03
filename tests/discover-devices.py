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

def main():
    print("Starting PreFormServer...")
    with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer):
        print("PreFormServer started successfully.")
        
        print("Scanning for printers...")
        api = PreFormApi()
        discovered_devices = api.discover_devices()

        if discovered_devices and discovered_devices['count'] > 0:
            real_devices = [device for device in discovered_devices['devices'] if is_real_printer(device)]
            print(f"Found {len(real_devices)} real device(s):")
            for device in real_devices:
                device_details = api.get_device_details(device['id'])
                if device_details:
                    print_device_info(device_details)
        else:
            print("No devices found.")

if __name__ == "__main__":
    main()