import json

namespace = "org.openegiz.oilguard"
twins = {}

twins[f"{namespace}:oilfield-01"] = {
    "policyId": "default:basic_policy",
    "attributes": {
        "name": "OilGuard AI Oil Field",
        "_isType": False,
        "kind": "oilfield"
    },
    "features": {
        "status": {"properties": {"value": "NORMAL"}},
        "active_wells": {"properties": {"value": 3, "unit": "wells"}}
    }
}

for number in range(1, 4):
    well = f"WELL-{number:02d}"
    twins[f"{namespace}:{well}"] = {
        "policyId": "default:basic_policy",
        "attributes": {
            "name": well,
            "_isType": False,
            "_parents": f"{namespace}:oilfield-01",
            "kind": "oil-well"
        },
        "features": {
            "pressure": {"properties": {"value": 0, "unit": "bar"}},
            "temperature": {"properties": {"value": 0, "unit": "C"}},
            "vibration": {"properties": {"value": 0, "unit": "mm/s"}},
            "status": {"properties": {"value": "NORMAL"}}
        }
    }

with open("oilguard_twins.json", "w", encoding="utf-8") as file:
    json.dump(twins, file, indent=2)

print("OilGuard AI digital twins created!")
print(f"Total twins: {len(twins)}")
