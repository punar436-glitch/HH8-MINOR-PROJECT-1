import json

def save_incident(incident, signature):
    record = {
        "incident_details": incident,
        "signature": signature
    }

    with open("incidents.json", "a") as file:
        json.dump(record, file)
        file.write("\n")

    print("Incident record saved successfully.")