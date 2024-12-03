import formlabs_local_api_minimal as formlabs
import requests
import pathlib
import sys
import json

pathToPreformServer = None
if sys.platform == 'win32':
    pathToPreformServer = pathlib.Path().resolve() / "C:\\Users\\avsimha\\PreFormServer\\PreFormServer.exe"
elif sys.platform == 'darwin':
    pathToPreformServer = pathlib.Path().resolve() / "PreFormServer.app/Contents/MacOS/PreFormServer"
else:
    print("Unsupported platform")
    sys.exit(1)
with formlabs.PreFormApi.start_preform_server(pathToPreformServer=pathToPreformServer):
    response = requests.request("GET", "http://localhost:44388/list-materials/")
    response.raise_for_status()
    json_result = response.json()
    with open("formlabs-materials-data.json", "w") as file:
        json.dump(json_result, file, indent=4, sort_keys=True)
        print("Materials data saved to formlabs-materials-data.json")
