import time
import requests

# TomTom API key
API_KEY = "fjbIvblscE9aaoZhczJxUaZQuJAeGtsu"

# List of diverse locations (Mumbai + Navi Mumbai)
locations = [
    {"name": "Dadar",     "lat": 19.0176, "lon": 72.8562},
    {"name": "Andheri",   "lat": 19.1197, "lon": 72.8468},
    {"name": "Powai",     "lat": 19.1197, "lon": 72.9051},
    {"name": "Colaba",    "lat": 18.9067, "lon": 72.8147},
    {"name": "Panvel",    "lat": 18.9894, "lon": 73.1175},
    {"name": "Airoli",    "lat": 19.1551, "lon": 72.9960},
    {"name": "Vashi",     "lat": 19.0760, "lon": 72.9986},
    {"name": "Nerul",     "lat": 19.0334, "lon": 73.0186},
    {"name": "Kharghar",  "lat": 19.0330, "lon": 73.0633}
]


import sqlite3
from datetime import datetime

def insert_traffic_data(location_name, lat, lon, current_speed, free_flow_speed, confidence, road_class, db_name="traffic_data.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    timestamp = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO traffic_data (
            location_name, lat, lon, timestamp,
            current_speed, free_flow_speed, confidence, road_class
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (location_name, lat, lon, timestamp,
          current_speed, free_flow_speed, confidence, road_class))

    conn.commit()
    conn.close()
    print(f"✅ Data inserted for {location_name} at {timestamp}")


# Fetch and insert traffic data for all locations
def fetch_and_store_all_locations():
    for loc in locations:
        try:
            url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json"
            params = {
                "point": f"{loc['lat']},{loc['lon']}",
                "key": API_KEY
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()["flowSegmentData"]

            insert_traffic_data(
                location_name = loc["name"],
                lat = loc["lat"],
                lon = loc["lon"],
                current_speed = data["currentSpeed"],
                free_flow_speed = data["freeFlowSpeed"],
                confidence = data["confidence"],
                road_class = data.get("roadClass", "Unknown")
            )
            print("done")

        except Exception as e:
            print(f"❌ Failed for {loc['name']}: {e}")

# Run every 15 minutes
if __name__ == "__main__":
    while True:
        print("\n⏳ Fetching traffic data for all locations...")
        fetch_and_store_all_locations()
        print("✅ All locations fetched and stored. Waiting 15 minutes...\n")
        time.sleep(15 * 60)  # Wait for 15 minutes (900 seconds)
