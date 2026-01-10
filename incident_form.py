def collect_incident():
    print("===== Incident Reporting Form =====")

    incident_type = input("Enter Incident Type: ")
    impact = input("Describe the Impact: ")
    evidence = input("Enter Evidence Details: ")
    resolution = input("Resolution Taken: ")

    incident = {
        "incident_type": incident_type,
        "impact": impact,
        "evidence": evidence,
        "resolution": resolution
    }

    return incident