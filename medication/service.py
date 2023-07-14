from database import get_db_connection

def get_medication_list():
    
    medication = [
        {
            "id": 12,
            "name": "Medication Name1",
            "schedule": "once a day",
            "time": "8:00 AM",
            "numberOfDoses": 3,
            "startDate": "2023-07-01",
            "endDate": "2023-07-31"
        }
    ]
    return medication

def add_medication(request_data):
    
    if "name" not in request_data or "schedule" not in request_data or "time" not in request_data or "numberOfDoses" not in request_data or "startDate" not in request_data or "endDate" not in request_data:
        return {"message": "Incomplete data. Please provide all required fields.", "status": "error"}

    # Extract data from request_data
    name = request_data["name"]
    schedule = request_data["schedule"]
    time = request_data["time"]
    numberOfDoses = request_data["numberOfDoses"]
    startDate = request_data["startDate"]
    endDate = request_data["endDate"]

    # Perform further validation and database insertion logic

    # Assuming the insertion was successful, return the response
    return {"message": "Medication added successfully.", "status": "success"}

def update_medication_by_id(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def delete_medication_by_id(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def update_medication_completion(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def get_medication_completion(medication_id):
    
    medication = {"name": "test"}
    
    return medication

def add_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
def view_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
def update_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
def delete_notes(notes_id):
    
    notes = {"name": "test"}
    
    return notes
