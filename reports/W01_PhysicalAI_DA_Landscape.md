# Week 1 Physical AI Data Analyst Landscape

## 1. Introduction

This report reviews InGen Dynamics' five physical AI platforms from a data analyst perspective. For each platform, it identifies the likely data sources, the main analytical questions, common data quality risks, and expected data formats.

The report also provides a data analyst interpretation of the six PIC 2.0 foundation model classes and summarises key references related to robotics sensor data, data quality, exploratory data analysis, and feature extraction.
## 2. InGen Platform Data Analyst Briefs

## 2. InGen Platform Data Analyst Briefs

| Platform | Likely Data Generated | Main Data Analysis Question | Likely Data Quality Issues | Expected Format |
|---|---|---|---|---|
| Fari | Response length, sentiment score, session duration, topic coherence, latency | What factors are associated with a high-quality companion interaction? | Missing feedback, inconsistent sentiment labels | Session-level CSV or JSON |
| Senpai | Student progress, session duration, quiz scores, response accuracy, topic history | Are learners improving over time, and which topics need additional support? | Missing sessions, inconsistent user identifiers | Learning-event CSV or database table |
| Sentinel Prime AI | Timestamped alerts, event type, location zone, severity, sensor status | Which zones and event types present the highest operational risk? | Duplicate alerts, missing severity, timestamp errors | Event log or JSON stream |
| Aido Rover | GPS, LiDAR, battery SoC, wheel torque, temperature, operational status | Is the rover operating within normal parameters, and what signals indicate possible faults? | GPS dropout, LiDAR saturation, torque noise spikes | Time-series CSV |
| Aido Humanoid | Joint velocity, joint position, balance metrics, motion mode, actuator temperature | Which motion mode is active, and are there signs of unstable movement? | Sensor drift, timestamp mismatch, motion-label errors | Time-series CSV |

### 2.1 Fari

Fari is an eldercare companion platform. A data analyst would likely examine interaction-level data such as response latency, sentiment, topic coherence, and session duration. The main objective would be to identify which session characteristics are associated with positive or high-quality user interactions.

### 2.2 Senpai

Senpai is an educational robot. Relevant data could include learner progress, quiz accuracy, session duration, and topic history. A data analyst could use this information to determine whether students are improving and which learning areas require additional support.

### 2.3 Sentinel Prime AI

Sentinel Prime AI generates timestamped security and alert events. A data analyst could compare event frequency by zone, event type, and severity to support patrol scheduling and risk monitoring.

### 2.4 Aido Rover

Aido Rover is the primary data anchor for this internship. It may generate GPS, LiDAR, battery, wheel torque, and temperature data. These time-series signals can be used to identify normal, warning, and fault conditions.

### 2.5 Aido Humanoid

Aido Humanoid may generate joint position, joint velocity, actuator, balance, and motion-mode data. Analysis could help identify movement patterns and detect unstable or abnormal operation.
v、## 3. PIC 2.0 Data Pipeline Map

| PIC 2.0 Model Class | Data Analyst Support |
|---|---|
| GRPO | Analyze reward scores, optimisation logs, model iteration results, and performance trends. |
| STUM | Process time-series sensor streams and identify temporal patterns or abnormal changes. |
| SEOM | Analyze environmental observations, event logs, and operational context data. |
| AMDC | Combine and compare multiple sensor modalities such as vision, LiDAR, GPS, and telemetry. |
| HTD-IRL | Analyze robot trajectories, expert demonstrations, action sequences, and learned behaviour patterns. |
| CRL-MRS | Analyze coordination, communication, task completion, and performance data across multiple robots. |
The role of the data analyst is not necessarily to design each foundation model. Instead, the analyst prepares, validates, summarises, and monitors the data that supports model training, testing, and deployment.
## 4. Reference Summaries

### Reference 1: InGen Product and PIC 2.0 Documentation

**Main topic:** InGen's physical AI platforms and the Origami AI PIC 2.0 architecture.

**Key takeaway:** Each InGen platform produces a different combination of sensor, event, interaction, and performance data.

**Internship relevance:** The product documentation helps connect data analysis tasks to specific InGen deployment scenarios.

### Reference 2: Mobile Robot Sensor Data Analysis

**Main topic:** GPS, LiDAR, IMU, battery, and other mobile robot telemetry.

**Key takeaway:** Robot sensor data is normally time-dependent and must be aligned through timestamps before analysis.

**Internship relevance:** This supports the Week 2 synthetic Aido Rover telemetry design.

### Reference 3: Data Quality in Industrial IoT and Robotics

**Main topic:** Missing values, sensor drift, saturation, noise, and timestamp errors.

**Key takeaway:** Sensor data should be validated before visualisation, statistical analysis, or predictive modelling.

**Internship relevance:** Every internship notebook begins with a mandatory data quality section.

### Reference 4: Exploratory Data Analysis Best Practices

**Main topic:** Dataset structure, missing values, distributions, correlations, outliers, and visualisation.

**Key takeaway:** EDA should move from general dataset inspection to more specific relationship and anomaly analysis.

**Internship relevance:** This provides the structure for the Week 2 EDA notebook.

### Reference 5: Computer Vision and Time-Series Feature Extraction

**Main topic:** The connection between extracting features from images and extracting features from sensor signals.

**Key takeaway:** Both computer vision and time-series analysis identify signal characteristics that distinguish normal and abnormal conditions.

**Internship relevance:** This connects the FiberHome computer vision experience to the Week 5 sensor feature analysis.

## 4. Reference Summaries

### Reference 1: InGen Product and PIC 2.0 Documentation

**Main topic:** InGen's physical AI platforms and the Origami AI PIC 2.0 architecture.

**Key takeaway:** Each InGen platform produces a different combination of sensor, event, interaction, and performance data.

**Internship relevance:** The product documentation helps connect data analysis tasks to specific InGen deployment scenarios.

### Reference 2: Mobile Robot Sensor Data Analysis

**Main topic:** GPS, LiDAR, IMU, battery, and other mobile robot telemetry.

**Key takeaway:** Robot sensor data is normally time-dependent and must be aligned through timestamps before analysis.

**Internship relevance:** This supports the Week 2 synthetic Aido Rover telemetry design.

### Reference 3: Data Quality in Industrial IoT and Robotics

**Main topic:** Missing values, sensor drift, saturation, noise, and timestamp errors.

**Key takeaway:** Sensor data should be validated before visualisation, statistical analysis, or predictive modelling.

**Internship relevance:** Every internship notebook begins with a mandatory data quality section.

### Reference 4: Exploratory Data Analysis Best Practices

**Main topic:** Dataset structure, missing values, distributions, correlations, outliers, and visualisation.

**Key takeaway:** EDA should move from general dataset inspection to more specific relationship and anomaly analysis.

**Internship relevance:** This provides the structure for the Week 2 EDA notebook.

### Reference 5: Computer Vision and Time-Series Feature Extraction

**Main topic:** The connection between extracting features from images and extracting features from sensor signals.

**Key takeaway:** Both computer vision and time-series analysis identify signal characteristics that distinguish normal and abnormal conditions.

**Internship relevance:** This connects the FiberHome computer vision experience to the Week 5 sensor feature analysis.
## 5. FiberHome Experience Connection

The Aido Rover data quality challenges are the most similar to the preprocessing challenges I encountered during my computer vision internship at FiberHome.

GPS dropout is similar to missing or corrupted image regions. LiDAR saturation is similar to overexposed or clipped image pixels. Wheel torque noise spikes are similar to visual noise or artifacts in image data.

In both computer vision and robot telemetry analysis, data must be tested, cleaned, and validated before meaningful conclusions or models can be produced.
## 6. Conclusion

The five InGen platforms generate different forms of physical AI data, including time-series sensor telemetry, security event logs, interaction records, learning progress data, and humanoid motion signals.

Although the data types differ, the same data analyst principles apply across all platforms:

1. Validate data quality before analysis.
2. Document missing values, abnormal ranges, and inconsistent labels.
3. Use analysis to answer a specific operational or product question.
4. Present findings in a form that supports business and deployment decisions.