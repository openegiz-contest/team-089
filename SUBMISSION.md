# SUBMISSION

<!-- Fill in every section. The AI Jury studies this file together with the code, the Build Report, the presentation and the Stand's interface. Accepted languages: English, Kazakh, Russian. These hint comments may be deleted. -->


## Concept


**Enterprise:** OilGuard AI — a digital twin of a fictional onshore oil production field inspired by oil-producing facilities in western Kazakhstan. The implemented model focuses on three production wells and their pressure, temperature and vibration measurements.

**Users:** Oil field operators, production engineers, maintenance teams and industrial safety specialists.

**Decision:** The digital twin helps operators decide when to reduce production, stop potentially dangerous equipment, inspect a pipeline or schedule preventive maintenance. The current prototype detects abnormal pressure, temperature and vibration using fixed thresholds. Operational risk prediction and corrective-action comparison are future development goals.

**Why this choice:** Oil and gas production involves interconnected equipment where failures may cause environmental damage, production losses and safety incidents. A digital twin makes these relationships visible and allows operators to test emergency scenarios without endangering real equipment. The current OilGuard AI prototype combines synthetic telemetry simulation, threshold-based safety detection and local visualization.

**Real or fictional:** The field is fictional and inspired by onshore oil production facilities in Kazakhstan, including the general operating characteristics of mature oil fields in the Mangystau region. All initial measurements and operating conditions are synthetic. Numerical parameters will be documented as engineering assumptions or supported by publicly available technical references where possible. The project does not claim access to confidential field data.
## Team

<!-- GitHub usernames of the Participants. Other personal data are not required: the repository becomes public after the Freeze (Rules, section 15). -->

| GitHub |
|---|
| эрасылтургенгул |

## Mine

OilGuard AI represents a fictional onshore oil production field in western Kazakhstan.

The digital twin model contains four objects:

- **oilfield-01:** Parent object representing the oil field.
- **WELL-01:** Production well with pressure, temperature and vibration monitoring.
- **WELL-02:** Production well with a simulated abnormal-pressure incident.
- **WELL-03:** Production well operating under normal conditions.

All three wells are linked to the parent oil field through the `_parents` attribute.

Twin definitions: `oilguard_twins.json`.

Twin generation: `create_oilguard_twins.py`.

Simulation: `oilguard_simulator.py`.

MQTT telemetry preparation: `oilguard_mqtt.py`.

The twins are defined locally but have not yet been verified on a running OpenEgiz Stand.

## Modules and What-if Scenarios

OilGuard AI currently provides local simulation and rule-based safety monitoring.

| Module or What-if Scenario | What it does | How to see it on the Stand | How to undo it (scenarios) |
|---|---|---|---|
| Well monitoring | Simulates pressure, temperature and vibration for three production wells. | Not yet deployed; local CSV and chart are available. | Not applicable |
| Safety detection | Assigns NORMAL or DANGER based on defined sensor thresholds. | Verified locally using MQTT dry-run output. | Not applicable |
| High-pressure incident | Simulates an abnormal operating period for WELL-02 between minutes 70 and 90. | Visible in oilguard_chart.png; not yet controllable on the Stand. | Regenerate the baseline simulation |

Current detection thresholds:
- Pressure greater than 80 bar.
- Temperature greater than 90 degrees Celsius.
- Vibration greater than 7 mm/s.

These thresholds are illustrative simulation assumptions, not certified industrial safety limits.

Interactive What-if controls on the OpenEgiz Stand are planned but not yet implemented.

## What works and what does not

### Verified locally
- Python simulation generates 360 telemetry records for three wells.
- The simulation includes 21 DANGER records for WELL-02.
- Pressure monitoring chart is generated successfully.
- Four digital twin definitions are generated in JSON.
- MQTT messages follow the Ditto modify-features structure.
- NORMAL and DANGER messages were verified using dry-run mode.

### Not yet verified
- Registration of the twins in a running OpenEgiz Stand.
- Live MQTT delivery to the platform.
- Grafana dashboard integration.
- Interactive What-if controls.

## Data and Assumptions

All measurements are synthetic and generated using Python.

Dataset: `oilguard_data.csv`.

Generator: `oilguard_simulator.py`.

The dataset contains:
- Three production wells.
- 120 simulated minutes.
- 360 telemetry records.
- Pressure in bar.
- Temperature in degrees Celsius.
- Vibration in mm/s.
- NORMAL and DANGER status labels.

A high-risk incident is simulated for WELL-02 during minutes 70 through 90.

The random seed is 42, making the generated dataset reproducible.

Safety thresholds are illustrative engineering assumptions:
- Pressure > 80 bar.
- Temperature > 90 C.
- Vibration > 7 mm/s.

These values are not validated against a specific real-world facility.

No confidential industrial data or personal information is used.

## Mine visualization

OilGuard AI currently provides a local pressure monitoring chart.

Visualization file: `oilguard_chart.png`.

The chart displays:
- Pressure measurements for WELL-02 over 120 simulated minutes.
- A red dashed line marking the 80 bar warning threshold.
- A highlighted abnormal operating period between minutes 70 and 90.

The chart is generated using `oilguard_chart.py`.

OpenEgiz Grafana dashboard integration is not yet completed.
There is currently no verified Stand URL for the OilGuard AI visualization.

## Limitations

- All sensor measurements are synthetic.
- The current model represents three wells and one parent oil field.
- Pressure, temperature and vibration are simulated independently.
- The model does not yet calculate physical fluid flow or reservoir dynamics.
- Detection uses fixed thresholds rather than a trained machine learning model.
- The high-pressure incident is predefined rather than controlled interactively.
- Live OpenEgiz deployment and Grafana visualization remain unverified.
- The model is a demonstration and must not be used for real industrial safety decisions.

## Presentation

`presentation.pdf` is available in the repository root. No video submitted.

---

Platform: OpenEgiz v1.0.4.
