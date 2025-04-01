import json, random, time
from datetime import datetime

def generate_sensor_data():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "vibration": round(random.uniform(0.1, 1.5), 2),
        "temperature": round(random.uniform(20, 90), 2),
        "pressure": round(random.uniform(1.0, 3.0), 2)
    }

while True:
    data = generate_sensor_data()
    with open("sensor_input.json", "w") as f:
        json.dump(data, f)
    print("Sensor data written:", data)
    time.sleep(1)
