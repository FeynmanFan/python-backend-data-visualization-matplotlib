import json
import random
from datetime import datetime, timedelta

def generate_record():
    route = random.choice(['/', '/login', '/catalog'])
    status_roll = random.random()
    if status_roll < 0.95:
        status = 200
    elif status_roll < 0.98:
        status = 500
    else:
        status = 302
    
    duration = round(random.uniform(0.5, 3.6), 2)  # Round to 2 decimal places for seconds
    
    # Generate a random time between 10:00 AM and 11:00 AM CST on February 14, 2024
    base_time = datetime(2024, 2, 14, 10, 0, 0)  # 10 AM CST
    random_time = base_time + timedelta(seconds=random.randint(0, 3600))  # Add up to 3600 seconds (1 hour)
    
    return {
        "route": route, 
        "status": status, 
        "duration": duration,
        "date": random_time.isoformat() + "-06:00"  # CST is UTC-6
    }

records = [generate_record() for _ in range(200)]

with open('data.json', 'w') as f:
    json.dump(records, f, indent=2)