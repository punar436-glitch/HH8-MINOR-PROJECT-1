from incident_form import collect_incident
from signature import generate_signature
from storage import save_incident

def main():
    incident = collect_incident()
    investigator = input("Enter Investigator Name: ")

    signature = generate_signature(investigator)
    save_incident(incident, signature)

if __name__ == "__main__":
    main()