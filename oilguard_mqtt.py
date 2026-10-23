import argparse
import csv
import json
import time

NAMESPACE = "org.openegiz.oilguard"

def make_message(well, row):
    features = {
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

    return {
        "topic": f"{NAMESPACE}/{well}/things/twin/commands/modify",
        "path": "/features",
        "value": features
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--steps", type=int, default=0)
    parser.add_argument("--mqtt-host", default="localhost")
    parser.add_argument("--mqtt-port", type=int, default=1883)
    parser.add_argument("--interval", type=float, default=2)
    args = parser.parse_args()

    client = None

    if not args.dry_run:
        import paho.mqtt.client as mqtt
        client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2,
            client_id="oilguard-ai"
        )
        client.connect(args.mqtt_host, args.mqtt_port)
        client.loop_start()

    with open("oilguard_data.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            well = row["well_id"]
            message = make_message(well, row)
            payload = json.dumps(message)

            if args.dry_run:
                print(payload)
            else:
                client.publish(
                    f"telemetry/{well}",
                    payload,
                    qos=0
                )
                time.sleep(args.interval)

            if args.steps and index + 1 >= args.steps:
                break

    if client:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
