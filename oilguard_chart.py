import csv
import matplotlib.pyplot as plt

minutes = []
pressures = []

with open("oilguard_data.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["well_id"] == "WELL-02":
            minutes.append(len(minutes))
            pressures.append(float(row["pressure_bar"]))

plt.figure(figsize=(12, 6))
plt.plot(minutes, pressures, color="blue", label="WELL-02 Pressure")
plt.axhline(80, color="red", linestyle="--", label="Danger limit")
plt.axvspan(70, 90, color="red", alpha=0.15, label="Simulated fault")
plt.xlabel("Time (minutes)")
plt.ylabel("Pressure (bar)")
plt.title("OilGuard AI - Oil Well Monitoring")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("oilguard_chart.png", dpi=200)
print("Chart saved: oilguard_chart.png")
plt.show()
