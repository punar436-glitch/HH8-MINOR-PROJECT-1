import hashlib
import datetime

def generate_signature(investigator_name):
    timestamp = str(datetime.datetime.now())
    raw_data = investigator_name + timestamp

    signature = hashlib.sha256(raw_data.encode()).hexdigest()

    return {
        "investigator": investigator_name,
        "timestamp": timestamp,
        "digital_signature": signature
    }