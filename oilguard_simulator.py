
import csv
import random
from datetime import datetime, timedelta

random.seed(42)

START = datetime(2026, 10, 23, 8, 0)
records = []

for minute in range(120):
    timestamp = START + timedelta(minutes=minute)

    for well in ["WELL-01", "WELL-02", "WELL-03"]:
        pressure = round(random.uniform(45, 65), 2)
        temperature = round(random.uniform(50, 75), 2)
        vibration = round(random.uniform(1, 4), 2)

        # Simulated equipment fault
        if well == "WELL-02" and 70 <= minute <= 90:
            pressure += 35
            temperature += 25
            vibration += 5

        if pressure > 80 or temperature > 90 or vibration > 7:
            status = "DANGER"
        else:
            status = "NORMAL"

        records.append([
            timestamp.isoformat(),
            well,
            pressure,
            temperature,
            vibration,
            status
        ])

with open("oilguard_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "timestamp",
        "well_id",
        "pressure_bar",
        "temperature_c",
        "vibration_mm_s",
        "status"
    ])
    writer.writerows(records)

danger_count = sum(row[5] == "DANGER" for row in records)

print("OilGuard AI simulation completed!")
print(f"Total records: {len(records)}")
print(f"Danger records: {danger_count}")
print("Dataset saved: oilguard_data.csv")
