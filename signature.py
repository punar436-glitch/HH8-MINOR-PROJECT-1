import hashlib
import datetime

def generate_signature(incident_id, investigator, timestamp):
    data = f"{incident_id}{investigator}{timestamp}"
    return hashlib.sha256(data.encode()).hexdigest()
