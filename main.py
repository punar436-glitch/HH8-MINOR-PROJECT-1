from incident_form import collect_incident
from storage import save_incident, view_incidents, search_incident, send_to_server

def menu():
    print("\n--- Incident Reporting System ---")
    print("1. Report New Incident")
    print("2. View All Incidents")
    print("3. Search Incident by ID")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        incident = collect_incident()
        save_incident(incident)
        send_to_server(incident)
        print("Incident recorded successfully!")

    elif choice == "2":
        view_incidents()

    elif choice == "3":
        iid = input("Enter Incident ID: ")
        search_incident(iid)

    elif choice == "4":
        print("Exiting system...")
        break

    else:
        print("Invalid choice!")
