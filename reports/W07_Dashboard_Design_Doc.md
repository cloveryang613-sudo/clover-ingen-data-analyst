# Week 7 Dashboard Design Document

**Intern:** Clover Yang  
**Role:** Data Analyst Intern  
**Project:** InGen Dynamics Data Analysis Dashboard

## 1. Dashboard Objective

The dashboard integrates outputs from the Week 5 feature analysis and the
Week 6 automated reporting pipeline.

Its purpose is to present Aido Rover fleet-health metrics, anomaly indicators,
and feature importance results in a format that can be understood by analysts,
product managers, and executives.

The dashboard uses pre-computed CSV and PNG files stored in the
`dashboard/data/` directory. No model training or major data processing is
performed when the dashboard launches.

## 2. View 1: Fleet Health Overview

### Target Persona

Product managers and operations teams.

### Headline Finding

The Aido Rover dataset has an average battery state of charge of approximately
59.99%, with 600 timesteps classified as high-risk anomaly periods.

### Data Sources

- `rover_kpi_summary.csv`
- `battery_soc_trend.png`
- `fault_rate.png`
- `top_anomalies.png`

### Main Elements

The view displays:

- Average battery state of charge
- Fault rate
- Average LiDAR distance
- High-risk anomaly count
- Battery trend
- Fault-rate trend
- Top anomaly periods

### Decision Supported

This view helps operations teams identify whether fleet health is stable and
whether maintenance investigation is required.

## 3. View 2: Feature Intelligence

### Target Persona

Data analysts and engineering teams.

### Headline Finding

Aido Rover operating status depends on several temporal and frequency-domain
features, while Fari interaction quality is strongly influenced by response
length and sentiment.

### Data Sources

- `rover_feature_importance.csv`
- `fari_feature_importance.csv`
- `rover_feature_importance.png`
- `fari_feature_importance.png`

### Main Elements

The view displays the highest-ranked features for both Aido Rover and Fari.

For Aido Rover, the leading features include battery rolling mean, battery
rolling standard deviation, LiDAR rolling statistics, rate-of-change features,
and wheel-torque spectral power.

For Fari, response length and sentiment score are the strongest predictors of
interaction quality.

### Decision Supported

This view helps analysts determine which sensor and interaction features should
receive the most attention in future monitoring systems.

## 4. View 3: KPI Monitoring

### Target Persona

Executives and product managers.

### Headline Finding

A small number of clearly defined KPIs can summarize the operational condition
of each InGen platform and connect technical data to business decisions.

### Data Sources

- `W06_KPI_Framework.md`
- `rover_kpi_summary.csv`

### Main Elements

The view is designed to display platform KPIs for:

- Aido Rover
- Sentinel Prime AI
- Fari
- Senpai
- Aido Humanoid

Each KPI includes its definition, measurement method, update frequency, and
decision link.

### Decision Supported

This view helps managers identify which platform requires attention and what
action should be taken when a KPI crosses its threshold.

## 5. Executive View

The executive view is designed to communicate three key numbers without
requiring detailed technical interpretation:

1. Average battery state of charge
2. Fault rate
3. Number of high-risk anomaly periods

The recommended monitoring priority is to review the highest anomaly periods
and determine whether they are associated with battery instability, LiDAR
variation, or wheel-torque imbalance.

## 6. Technical Design

The dashboard code is stored in:

`dashboard/app.py`

The dashboard loads only pre-computed outputs from:

`dashboard/data/`

This design separates data processing from presentation. Feature engineering,
model training, and KPI calculation are completed in earlier notebooks.

The intended launch command is:

```bash
streamlit run dashboard/app.py