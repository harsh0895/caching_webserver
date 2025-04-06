import time

def fetch_data():
    # Simulate a slow DB/API response
    time.sleep(2)
    return {"message": "This is data from the database!"}
