import random
import json
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Predefined data pools
problem_list_pool = [
    "Hypertension", "Diabetes", "Asthma", "Migraines", "Arthritis",
    "Cholesterol", "Anxiety", "Depression", "Obesity", "Back Pain", "Other"
]

medications_pool = [
    "Paracetamol", "Amoxicillin", "Metformin", "Ibuprofen", "Atorvastatin",
    "Omeprazole", "Amlodipine", "Lisinopril", "Albuterol", "Prednisone", "Other"
]

allergies_pool = [
    "Penicillin", "Pollen", "Dust", "Nuts", "Shellfish",
    "Ibuprofen", "Latex", "Milk", "Eggs", "Soy", "Other"
]

lbf_codes = [
    ("LBF101", lambda: f"{round(random.uniform(3.5, 7.0), 1)}"),     # Blood Glucose
    ("LBF102", lambda: f"{round(random.uniform(11.0, 16.0), 1)}"),   # Hemoglobin
    ("LBF103", lambda: f"{random.randint(100, 130)}/{random.randint(70, 90)}"),  # Blood Pressure
]

# Generate a single record
def generate_record(index):
    record_id = f"HR-{index:03d}"
    patient_id = f"PAT-{random.randint(10000, 99999)}"
    name = fake.name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
    date_of_service = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat() + "+0000"
    doctor_id = f"DR-{random.randint(10000, 99999)}"
    complaint = random.sample(["Headache", "Fever", "Cough", "Nausea", "Fatigue", "Blurred vision"], k=2)
    allergies = random.sample(allergies_pool, k=3)
    medications = random.sample(medications_pool, k=3)
    problems = random.sample(problem_list_pool, k=3)
    sex = random.choice(["Male", "Female", "Other"])
    address = fake.street_address()
    city = "Colombo"
    state = "Western"
    zip_code = "00700"
    phone = f"07{random.randint(10000000, 99999999)}"
    lbf_data = [f"{code}:{value_gen()}" for code, value_gen in lbf_codes]
    his_data = [f"HIS{str(random.randint(1, 9)).zfill(3)}" for _ in range(2)]

    return {
        "record_id": record_id,
        "patient_id": patient_id,
        "patient_name": name,
        "patient_dob": dob,
        "date_of_service": date_of_service,
        "referring_doctor": doctor_id,
        "chief_complaint": complaint,
        "allergies": allergies,
        "medications": medications,
        "problem_list": problems,
        "patient_sex": sex,
        "address": address,
        "city": city,
        "state": state,
        "zip": zip_code,
        "patient_phone": phone,
        "lbf_data": lbf_data,
        "his_data": his_data
    }

# Generate all records
records = [generate_record(i + 1) for i in range(5)]

# Save to JSON file
with open("health_records-5.json", "w") as f:
    json.dump(records, f, indent=2)
    print("✅ 5 records generated and saved to 'health_records.json'")

# Generate all records
records = [generate_record(i + 1) for i in range(1000)]

# Save to JSON file
with open("health_records-1000.json", "w") as f:
    json.dump(records, f, indent=2)
    print("✅ 1000 records generated and saved to 'health_records.json'")

# Generate all records
records = [generate_record(i + 1) for i in range(1000)]

# Save to JSON file
with open("health_records-10000.json", "w") as f:
    json.dump(records, f, indent=2)
    print("✅ 10000 records generated and saved to 'health_records.json'")

# Generate all records
records = [generate_record(i + 1) for i in range(1000)]

# Save to JSON file
with open("health_records-100000.json", "w") as f:
    json.dump(records, f, indent=2)
    print("✅ 100000 records generated and saved to 'health_records.json'")
