import json
from pathlib import Path

source = Path("examples/mine/dashboard.json")
target = Path("examples/oilguard/dashboard.json")

dashboard = json.loads(source.read_text(encoding="utf-8-sig"))

dashboard["uid"] = "oilguard-ai-dashboard"
dashboard["title"] = "OilGuard AI - Oil Field Safety"
dashboard["tags"] = ["openegiz", "oilguard", "safety"]
dashboard["description"] = "OilGuard AI: monitoring pressure, temperature and vibration in simulated oil wells."

fields = [
    ("Pressure - WELL-02", "pressure_properties_value", "pressure", 80),
    ("Temperature - WELL-02", "temperature_properties_value", "celsius", 90),
    ("Vibration - WELL-02", "vibration_properties_value", "velocityms", 7),
]

panels = []

for i, (title, field, unit, threshold) in enumerate(fields):
    panel = {
        "id": i + 1,
        "type": "timeseries",
        "title": title,
        "datasource": {
            "type": "influxdb",
            "uid": "opentwins-influxdb"
        },
        "gridPos": {
            "x": 0,
            "y": i * 8,
            "w": 24,
            "h": 8
        },
        "fieldConfig": {
            "defaults": {
                "unit": unit,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "red", "value": threshold}
                    ]
                }
            },
            "overrides": []
        },
        "targets": [
            {
                "refId": "A",
                "datasource": {
                    "type": "influxdb",
                    "uid": "opentwins-influxdb"
                },
                "query": (
                    'from(bucket: "default")\n'
                    '  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\n'
                    '  |> filter(fn: (r) => '
                    'r.thingId == "org.openegiz.oilguard:WELL-02" '
                    f'and r._field == "{field}")'
                )
            }
        ]
    }
    panels.append(panel)

dashboard["panels"] = panels

target.write_text(
    json.dumps(dashboard, indent=2),
    encoding="utf-8"
)

print("Dashboard created:", target)
print("Panels:", len(panels))
