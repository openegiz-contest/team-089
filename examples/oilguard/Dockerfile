FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY oilguard_mqtt.py setup_twins.py twins.json oilguard_data.csv ./

USER nobody

CMD ["python", "oilguard_mqtt.py"]
