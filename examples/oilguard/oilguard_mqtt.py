import argparse
import csv
import json
import time
from pathlib import Path

NAMESPACE = "org.openegiz.oilguard"


def make_message(well, row):
    return {
        "topic": f"{NAMESPACE}/{well}/things/twin/commands/modify",
        "path": "/features",
        "value": {
            "pressure": {
                "properties": {
                    "value": float(row["pressure_bar"]),
                    "unit": "bar"
                }
            },
            "temperature": {
                "properties": {
                    "value": float(row["temperature_c"]),
                    "unit": "C"
                }
            },
            "vibration": {
                "properties": {
                    "value": float(row["vibration_mm_s"]),
                    "unit": "mm/s"
                }
            },
            "status": {
                "properties": {
                    "value": row["status"]
                }
            }
        }
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--steps", type=int, default=0)
    parser.add_argument("--mqtt-host", default="localhost")
    parser.add_argument("--mqtt-port", type=int, default=1883)
    parser.add_argument("--interval", type=float, default=2.0)
    args = parser.parse_args()

    csv_path = Path(__file__).with_name("oilguard_data.csv")

    if not csv_path.exists():
        print(f"ERROR: CSV file not found: {csv_path}")
        return

    client = None

    try:
        if not args.dry_run:
            import paho.mqtt.client as mqtt

            client = mqtt.Client(
                mqtt.CallbackAPIVersion.VERSION2,
                client_id="oilguard-ai"
            )
            client.connect(args.mqtt_host, args.mqtt_port)
            client.loop_start()

        published = 0

        while True:
            with open(csv_path, encoding="utf-8") as file:
                reader = csv.DictReader(file)
                rows_in_cycle = 0

                for row in reader:
                    well = row["well_id"]
                    payload = json.dumps(make_message(well, row))

                    if args.dry_run:
                        print(payload)
                    else:
                        client.publish(f"telemetry/{well}", payload, qos=0)

                        if row["status"] == "DANGER":
                            print(f"ALERT: {well} DANGER", flush=True)

                        time.sleep(args.interval)

                    published += 1
                    rows_in_cycle += 1

                    if args.steps and published >= args.steps:
                        return

                if rows_in_cycle == 0:
                    print("ERROR: CSV file is empty.")
                    return

    except KeyboardInterrupt:
        print("Simulator stopped.")

    finally:
        if client:
            client.loop_stop()
            client.disconnect()


if __name__ == "__main__":
    main()
