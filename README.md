Multi-Sensor Signal Analysis & Anomaly Detection (Python)
📌 Overview

This project focuses on analyzing multi-sensor time-series data and detecting anomalies using statistical methods.
It simulates a real-world telemetry scenario where multiple sensor signals are monitored to identify abnormal behavior.

The goal is to build a simple, explainable, and reliable anomaly detection pipeline suitable for large-scale sensor data.

📊 Dataset Description

The dataset contains time-stamped sensor readings collected from an IoT environment.

Key columns used in this project:

ts – Unix timestamp of sensor reading

temp – Temperature sensor value

humidity – Humidity sensor value

The dataset is large (≈4 lakh rows), making it suitable for testing scalability and real-world data handling.

⚙️ Methodology
1. Data Preprocessing

Loaded data using Pandas

Converted Unix timestamps (ts) into readable datetime format

Selected relevant sensor columns for analysis

2. Anomaly Detection (Z-Score)

Used Z-score statistical method to detect anomalies

Applied the 3-sigma rule:

Values with |Z-score| > 3 are marked as anomalies

Implemented detection in a generic function, allowing reuse for multiple sensors

3. Multi-Sensor Analysis

Extended anomaly detection from a single sensor to multiple sensors

Currently applied to:

Temperature

Humidity

Each sensor has an independent anomaly flag

4. Visualization

Visualized sensor readings over time

Highlighted anomalous points separately

Used Matplotlib for clear interpretation

🧠 Why Statistical Methods?

Z-score is simple, interpretable, and reliable

Suitable for signal and telemetry data

Avoids black-box models, making results easier to explain

This approach aligns well with real-world monitoring systems where transparency is important.

🛠️ Technologies Used

Python

Pandas

Matplotlib

Git

▶️ How to Run

Clone the repository

Install dependencies:

pip install pandas numpy matplotlib


Run the analysis:

python analysis.py


The script will generate anomaly visualizations for each sensor.

🚀 Future Enhancements

Add comparison with other statistical methods (e.g., IQR)

Extend analysis to additional sensor signals

Aggregate signals over time windows to reduce noise

📌 Key Learning Outcomes

Handling large-scale time-series sensor data

Applying statistical anomaly detection

Designing modular and reusable analysis code

Visualizing and interpreting telemetry anomalies
