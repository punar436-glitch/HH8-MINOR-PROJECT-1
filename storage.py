import json
import os
import requests

FILE = "incidents.json"

def save_incident(incident):
    data = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append(incident)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def view_incidents():
    if not os.path.exists(FILE):
        print("No incidents found.")
        return

    with open(FILE, "r") as f:
        incidents = json.load(f)

    print("\n--- All Incidents ---")
    for inc in incidents:
        print("\n----------------------")
        for k, v in inc.items():
            print(f"{k}: {v}")

def search_incident(incident_id):
    incident_id = incident_id.strip().lower()

    if not os.path.exists(FILE):
        print("No data available.")
        return

    with open(FILE, "r") as f:
        incidents = json.load(f)

    for inc in incidents:
        if inc.get("incident_id", "").strip().lower().upper() == incident_id:
            print("\nIncident Found")
            for k, v in inc.items():
                print(f"{k}: {v}")
            return

    print("Incident ID not found.")


def send_to_server(incident):
    try:
        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=incident,
            timeout=5
        )
        if response.status_code == 201:
            print("Incident sent to server successfully.")
        else:
            print("Server responded, but incident not stored remotely.")
    except Exception:
        print("Server communication failed.")
def save_incident(incident):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
    except:
        data = []

    data.append(incident)

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
