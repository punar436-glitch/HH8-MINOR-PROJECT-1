from datetime import datetime
from signature import generate_signature

def collect_incident():
    print("\nEnter Incident Details")

    incident_id = input("Incident ID: ")
    date = input("Date (DD-MM-YYYY): ")
    impact = input("Impact: ")
    evidence = input("Evidence: ")
    resolution = input("Resolution: ")
    investigator = input("Investigator Name: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Open"

    signature = generate_signature(incident_id, investigator, timestamp)

    return {
        "incident_id": incident_id,
        "date": date,
        "impact": impact,
        "evidence": evidence,
        "resolution": resolution,
        "investigator": investigator,
        "status": status,
        "timestamp": timestamp,
        
    }

