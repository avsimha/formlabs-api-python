"""
Demo application of a Print Upload Dialog using the Formlabs Local API.

The application is meant to be demo of the API calls and logic involved in building a print upload dialog.
The model to be sliced and uploaded is a simple cube.stl file included in the same directory as this script.

The following are all left intentionally unfinished to keep the demo code concise:
- Loading user models
- Print preparation
- Application styling
- Deployment

Installation:
- On MacOS if using Python 3.12: brew install python-tk@3.12
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk  # themed tk
import atexit
import pathlib
import requests
import formlabs_local_api_minimal as formlabs
import sys
import time

pathToPreformServer = None
if sys.platform == "win32":
    pathToPreformServer = (
        pathlib.Path().resolve().parents[1] / "PreFormServer/PreFormServer.exe"
    )
elif sys.platform == "darwin":
    pathToPreformServer = (
        pathlib.Path().resolve().parents[1]
        / "PreFormServer.app/Contents/MacOS/PreFormServer"
    )
else:
    print("Unsupported platform")
    sys.exit(1)

TEST_FILE_PATH = pathlib.Path().resolve() / "cube.stl"
SLICING_PROGRESS_POLL_INTERVAL_S = 0.5
PRINTER_TYPES_THAT_SUPPORT_PRINTER_GROUPS = [
    "Form 3/3+",
    "Form 3B/3B+",
    "Form 3L",
    "Form 3BL",
    "Form 4",
    "Form 4B",
    "Form 4L",
    "Form 4BL",
]
MACHINE_TYPES_WITHIN_LABEL = {
    "Form 2": [
        "Form 2",
        "Form Cell",
    ],
    "Form 3/3+": [
        "Form 3",
        "Form 3+",
    ],
    "Form 3B/3B+": [
        "Form 3B",
        "Form 3B+",
    ],
    "Form 3L": [
        "Form 3L",
    ],
    "Form 3BL": [
        "Form 3BL",
    ],
    "Form 4": [
        "Form 4",
    ],
    "Form 4B": [
        "Form 4B",
    ],
    "Form 4L": [
        "Form 4L",
    ],
    "Form 4BL": [
        "Form 4BL",
    ],
    "Fuse 1": [
        "Fuse 1",
    ],
    "Fuse 1+ 30W": [
        "Fuse 1+ 30W",
    ],
}
PRINTER_GROUP_PRODUCT_NAME = "Printer Group"
PRINTABLE_PRODUCT_NAMES = []
for _, v in MACHINE_TYPES_WITHIN_LABEL.items():
    PRINTABLE_PRODUCT_NAMES.extend(v)
PRINTABLE_PRODUCT_NAMES.append(PRINTER_GROUP_PRODUCT_NAME)


def get_printer_dropdown_label(device):
    # Example: "FoamyPorcupine [Form 3] Idle"
    return f"{device['id']} [{device['product_name']}] {device['status']}"


def get_print_setting_dropdown_label(material_label, setting_label):
    # Example: "Alumina 4N V1 0.050 mm (Default Settings)"
    return f"{material_label} {setting_label}"


def get_printers():
    """Use the Formlabs Local API to get a list of available printers"""
    list_devices_response = requests.request(
        "GET",
        "http://localhost:44388/devices/",
    )
    list_devices_response.raise_for_status()
    available_printers = {}
    data = list_devices_response.json()
    for device in data["devices"]:
        if (
            device["is_connected"]
            and device["status"] != "Virtual Printer"
            and device["product_name"] in PRINTABLE_PRODUCT_NAMES
        ):
            available_printers[get_printer_dropdown_label(device)] = device
    return available_printers


def get_available_print_settings():
    """Use the Formlabs Local API to get a list of available print settings per printer type"""
    list_materials_response = requests.request(
        "GET",
        "http://localhost:44388/list-materials/",
    )
    list_materials_response.raise_for_status()
    data = list_materials_response.json()
    result = {}
    for v in data["printer_types"]:
        # Flatten the nested materials list into a single list of print settings per printer type
        flattened_materials = {}
        for m in v["materials"]:
            for s in m["material_settings"]:
                label = get_print_setting_dropdown_label(m["label"], s["label"])
                flattened_materials[label] = s["scene_settings"]
        result[v["label"]] = flattened_materials
    return result


def print_now():
    """Submit a print job to the selected printer with the selected print setting"""
    global progress_label_textvar, progress_label, progress_bar_value

    if not selected_printer.get():
        messagebox.showerror("Error", "No printer selected.")
        return
    if not selected_print_setting.get():
        messagebox.showerror("Error", "No print setting selected.")
        return
    if not job_name.get():
        messagebox.showerror("Error", "Job Name cannot be empty.")
        return

    selected_printer_id = available_printers[selected_printer.get()]["id"]
    print_setting_json = available_print_settings[selected_printer_type.get()][
        selected_print_setting.get()
    ]

    progress_label_textvar.set("Print operation started...")
    progress_label.update()
    progress_bar_value.set(0)
    progress_bar.grid()
    requests.request(
        "POST", "http://localhost:44388/scene/", json=print_setting_json
    ).raise_for_status()
    requests.request(
        "POST",
        "http://localhost:44388/scene/import-model/",
        json={
            "file": str(TEST_FILE_PATH),
        },
    ).raise_for_status()
    print_response = requests.request(
        "POST",
        "http://localhost:44388/scene/print/?async=true",
        json={
            "printer": selected_printer_id,
            "job_name": job_name.get(),
        },
    )
    print_response.raise_for_status()
    print_operation_id = print_response.json()["operationId"]
    # Long poll for task progress
    while True:
        status_response = requests.request(
            "GET",
            f"http://localhost:44388/operations/{print_operation_id}/",
        )
        status_response.raise_for_status()
        data = status_response.json()
        if data["status"] == "SUCCEEDED":
            progress_label_textvar.set("Print job uploaded successfully!")
            progress_label.update()
            progress_bar.grid_remove()  # hide progress bar
            break
        elif data["status"] == "FAILED":
            progress_label_textvar.set(
                f"Print job upload failed! Error: {data["result"]["error"]["message"]}"
            )
            progress_label.update()
            progress_bar.grid_remove()  # hide progress bar
            break
        else:
            progress_label_textvar.set(f"Progress: {data['progress']*100:.2f}%")
            progress_label.update()
            progress_bar_value.set(data["progress"] * 100)
            time.sleep(SLICING_PROGRESS_POLL_INTERVAL_S)


def get_filtered_printers_based_on_selected_printer_type(selected_printer_type):
    new_choices = []
    for k, v in available_printers.items():
        # TODO: figure out a way to avoid needing to hardcode this logic
        if v["product_name"] in MACHINE_TYPES_WITHIN_LABEL[selected_printer_type] or (
            v["product_name"] == PRINTER_GROUP_PRODUCT_NAME
            and selected_printer_type in PRINTER_TYPES_THAT_SUPPORT_PRINTER_GROUPS
        ):
            new_choices.append(k)
    return new_choices


def sync_selected_printer_dropdown():
    """Update the printer selection dropdown based on the selected printer type"""
    global selected_printer, printer_selection_menu, selected_printer_type
    printer_selection_menu["menu"].delete(0, "end")

    new_choices = get_filtered_printers_based_on_selected_printer_type(
        selected_printer_type.get()
    )
    for choice in new_choices:
        printer_selection_menu["menu"].add_command(
            label=choice, command=tk._setit(selected_printer, choice)
        )
    if len(new_choices) > 0:
        if selected_printer.get() not in new_choices:
            selected_printer.set(new_choices[0])
    else:
        selected_printer.set("")


def on_selected_printer_type_change(var, index, mode):
    """Update the printer and print settings dropdowns based on the selected printer type"""
    global selected_print_setting, print_setting_selection_menu
    sync_selected_printer_dropdown()

    print_setting_selection_menu["menu"].delete(0, "end")
    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = available_print_settings[selected_printer_type.get()]
    for choice in new_choices:
        print_setting_selection_menu["menu"].add_command(
            label=choice, command=tk._setit(selected_print_setting, choice)
        )
    if len(list(new_choices.keys())) > 0:
        selected_print_setting.set(list(new_choices.keys())[0])
    else:
        selected_print_setting.set("")


def on_add_printer_by_ip_pressed():
    """Use the Formlabs Local API to attempt to discover a printer at the given IP address"""
    ip_address = simpledialog.askstring(
        title="Add Printer by IP Address", prompt="Printer IP Address:"
    )
    if ip_address is not None and len(ip_address) > 0:
        add_printer_response = requests.request(
            "POST",
            "http://localhost:44388/discover-devices/",
            json={
                "timeout_seconds": 10,
                "ip_address": ip_address,
            },
        )
        if add_printer_response.status_code == 400:
            messagebox.showerror(
                "Error", "No printers found at the provided IP address."
            )
        elif add_printer_response.status_code == 200:
            add_printer_response_json = add_printer_response.json()
            if add_printer_response_json["count"] > 0:
                messagebox.showinfo("Success", f"Printer successfully added")
                get_printers_and_sync_dropdown()
            else:
                messagebox.showerror(
                    "Error", "No printers found at the provided IP address."
                )
                # Failing to find a printer an IP address could remove a printer from the list
                get_printers_and_sync_dropdown()
        else:
            add_printer_response.raise_for_status()


def on_login_button_pressed():
    """Use the Formlabs Local API to login to a user's Formlabs Account.
    Formlabs Accounts are needed for remote printing and Fleet Control uploads.
    """
    username = simpledialog.askstring(title="Login to Dashboard", prompt="Username:")
    if username is not None and len(username) > 0:
        password = simpledialog.askstring(
            title="Login to Dashboard", prompt="Password:"
        )
        if password is not None and len(password) > 0:
            login_response = requests.request(
                "POST",
                "http://localhost:44388/login/",
                json={
                    "username": username,
                    "password": password,
                },
            )
            if login_response.status_code == 200:
                messagebox.showinfo("Success", f"Logged in as {username}")
                # Refresh list of printers to include the new Printer Groups
                get_printers_and_sync_dropdown()
            else:
                messagebox.showinfo("Error", f"Login failed.")
                login_response.raise_for_status()


def discover_printers_button_pressed():
    """Use the Formlabs Local API to discover printers on the local network"""
    messagebox.showinfo("Discover Printers", f"Starting to Discover Printers for 10s")
    discovery_devices_response = requests.request(
        "POST",
        "http://localhost:44388/discover-devices/",
        json={"timeout_seconds": 10},
    )
    discovery_devices_response.raise_for_status()
    d = discovery_devices_response.json()
    get_printers_and_sync_dropdown()
    messagebox.showinfo(
        "Discover Printers", f"Discovery Finished. Found {d['count']} devices."
    )


def get_printers_and_sync_dropdown():
    global available_printers
    available_printers = get_printers()
    sync_selected_printer_dropdown()


################################ GUI Setup
root = tk.Tk()
root.title("Demo Print Dialog")
root.geometry("500x300")

################################# Start PreFormServer in background
print("Starting PreFormServer...")
local_api_server = formlabs.PreFormApi.start_preform_sync(
    pathToPreformServer=pathToPreformServer
)
print("PreFormServer started.")


################################# Stop PreFormServer on exit
def clean_up_preformserver():
    global local_api_server
    if local_api_server:
        local_api_server.stop_preform_server()
        print("PreFormServer stopped.")


atexit.register(clean_up_preformserver)


def _quit():
    root.quit()
    root.destroy()
    clean_up_preformserver()


root.protocol("WM_DELETE_WINDOW", _quit)

################################# UI Data:
available_print_settings = get_available_print_settings()
available_printer_types = list(available_print_settings.keys())
available_printers = get_printers()

################################# UI State Variables
selected_printer_type = tk.StringVar(root)
selected_printer_type.set(available_printer_types[0])
selected_printer = tk.StringVar(root)
selected_print_setting = tk.StringVar(root)
selected_print_setting.set(
    list(available_print_settings[selected_printer_type.get()].keys())[0]
)
job_name = tk.StringVar(root)
job_name.set("Test Job")
progress_label_textvar = tk.StringVar(root)
progress_bar_value = tk.DoubleVar()

################################# UI Elements:
top_frame = tk.Frame(root)
top_frame.pack(anchor="w", padx=10, pady=10)

web_login_button = tk.Button(
    top_frame,
    text="Formlabs Account Login",
    command=on_login_button_pressed,
)
web_login_button.grid(row=0, column=0, sticky="w")

add_printer_button = tk.Button(
    top_frame,
    text="Add Printer by IP",
    command=on_add_printer_by_ip_pressed,
)
add_printer_button.grid(row=0, column=1, sticky="w")

discover_printers_button = tk.Button(
    top_frame,
    text="Discover Printers",
    command=discover_printers_button_pressed,
)
discover_printers_button.grid(row=0, column=2, sticky="w")

frame = tk.Frame(root)
frame.pack(anchor="w", padx=10, pady=10)

printer_type_selection_label = tk.Label(frame, text="Printer Type: ")
printer_type_selection_label.grid(row=0, column=0, sticky="w")

printer_type_selection_menu = ttk.Combobox(
    frame, width=15, state="readonly", textvariable=selected_printer_type
)
printer_type_selection_menu["values"] = available_printer_types
printer_type_selection_menu.current(0)
printer_type_selection_menu.grid(row=0, column=1, sticky="w")

printer_selection_label = tk.Label(frame, text="Printer: ")
printer_selection_label.grid(row=1, column=0, sticky="w")

printer_selection_menu = tk.OptionMenu(frame, selected_printer, "")
printer_selection_menu.grid(row=1, column=1, sticky="w")

print_setting_selection_label = tk.Label(frame, text="Print Setting: ")
print_setting_selection_label.grid(row=2, column=0, sticky="w")

print_setting_selection_menu = tk.OptionMenu(
    frame,
    selected_print_setting,
    *available_print_settings[selected_printer_type.get()].keys(),
)
print_setting_selection_menu.grid(row=2, column=1, sticky="w")

job_name_label = tk.Label(frame, text="Job Name: ")
job_name_label.grid(row=3, column=0, sticky="w")
job_name_entry = tk.Entry(frame, textvariable=job_name)
job_name_entry.grid(row=3, column=1, sticky="w")

print_now_button = tk.Button(
    frame,
    text="Print Now",
    command=print_now,
)
print_now_button.grid(row=4, column=1, sticky="w")

bottom_frame = tk.Frame(root)
bottom_frame.pack(anchor="w", padx=10, pady=10)

progress_label = tk.Label(bottom_frame, textvariable=progress_label_textvar)
progress_label.grid(row=0, column=0, sticky="w")
progress_bar = ttk.Progressbar(
    bottom_frame,
    orient="horizontal",
    length=200,
    mode="determinate",
    variable=progress_bar_value,
)
progress_bar.grid(row=1, column=0, sticky="w")
progress_bar.grid_remove()  # Hide it initially

################################# Setup event handling after UI elements exist:
sync_selected_printer_dropdown()
selected_printer_type.trace_add("write", on_selected_printer_type_change)

################################# Run main event loop
root.mainloop()