from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer,
    Image, PageBreak, Table, TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from pathlib import Path

output = "presentation.pdf"
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="OilTitle",
    parent=styles["Title"],
    fontSize=28,
    leading=34,
    textColor=colors.HexColor("#123B55"),
    spaceAfter=24
))

styles.add(ParagraphStyle(
    name="OilHeading",
    parent=styles["Heading1"],
    fontSize=21,
    leading=26,
    textColor=colors.HexColor("#123B55"),
    spaceAfter=20
))

styles.add(ParagraphStyle(
    name="OilBody",
    parent=styles["BodyText"],
    fontSize=13,
    leading=21,
    spaceAfter=14
))

doc = SimpleDocTemplate(
    output,
    pagesize=(29.7 * cm, 21 * cm),
    rightMargin=2.3 * cm,
    leftMargin=2.3 * cm,
    topMargin=2 * cm,
    bottomMargin=2 * cm
)

story = []

def title(text):
    story.append(Paragraph(text, styles["OilHeading"]))

def body(text):
    story.append(Paragraph(text, styles["OilBody"]))

def page():
    story.append(PageBreak())

# PAGE 1
story.append(Spacer(1, 3 * cm))
story.append(Paragraph("OilGuard AI", styles["OilTitle"]))
body("Digital Twin for Oil Field Safety Monitoring")
body("OpenEgiz Digital Mine Competition")
body("Team: team-089 | Solo participant")
body("A fictional oil field inspired by western Kazakhstan.")
page()

# PAGE 2
title("1. The Problem")
body("Oil production equipment operates under changing pressure, temperature and vibration.")
body("Abnormal measurements can indicate potential equipment failures and safety risks.")
body("OilGuard AI demonstrates how a digital twin can help operators recognize dangerous conditions earlier.")
page()

# PAGE 3
title("2. Digital Twin Architecture")
body("The simulated oil field contains one parent digital twin and three production well twins.")
body("Parent: oilfield-01")
body("Wells: WELL-01, WELL-02 and WELL-03")
body("Each well has pressure, temperature, vibration and operational status features.")
body("Telemetry messages are prepared in the Eclipse Ditto protocol format for OpenEgiz integration.")
page()

# PAGE 4
title("3. Safety Detection Algorithm")
body("The Python simulator generates 360 telemetry records across 120 simulated minutes.")
body("A record is classified as DANGER if at least one illustrative threshold is exceeded:")
body("Pressure &gt; 80 bar")
body("Temperature &gt; 90 degrees Celsius")
body("Vibration &gt; 7 mm/s")
body("An abnormal event is introduced in WELL-02 during minutes 70 through 90.")
body("These thresholds are demonstration assumptions, not certified industrial limits.")
page()

# PAGE 5
title("4. Simulation Results")
body("360 total telemetry records | 3 wells | 21 DANGER records")
chart = Path("oilguard_chart.png")
if chart.exists():
    img = Image(str(chart))
    img.drawWidth = 22 * cm
    img.drawHeight = img.imageHeight * img.drawWidth / img.imageWidth
    if img.drawHeight > 11 * cm:
        img.drawHeight = 11 * cm
        img.drawWidth = img.imageWidth * img.drawHeight / img.imageHeight
    story.append(img)
else:
    body("Chart file not found.")
page()

# PAGE 6
title("5. Results and Next Steps")
body("Verified locally: dataset generation, safety status detection, pressure chart, four twin definitions and MQTT dry-run messages.")
body("Not yet verified: live OpenEgiz deployment, Grafana dashboard and interactive What-if controls.")
body("Next steps: connect the simulator to a running OpenEgiz Stand, visualize live telemetry and add operator-controlled scenarios.")
body("The model uses synthetic data and is not intended for real industrial safety decisions.")
body("Repository: github.com/openegiz-contest/team-089")

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.grey)
    canvas.drawRightString(27 * cm, 1 * cm, f"OilGuard AI | {doc.page}")
    canvas.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)

print("Presentation created:", output)
