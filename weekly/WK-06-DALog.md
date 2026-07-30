# Week 6 Data Analyst Log

**Intern:** Clover Yang  
**Role:** Data Analyst Intern  
**Week:** Week 6  
**Focus:** Automated Reporting Pipeline & KPI Framework


## What I Analyzed

This week, I developed an automated reporting pipeline for Aido Rover
telemetry data.

The pipeline was designed to transform raw sensor data into actionable
operational insights. The workflow included data ingestion, data quality
validation, feature generation, KPI calculation, anomaly detection summary,
chart generation, and automated report creation.

The pipeline calculated important fleet-health indicators including average
battery state of charge, fault rate, average LiDAR distance, wheel torque
imbalance, and anomaly score statistics.


## What I Found

The most important finding from this week was that automated reporting
requires clear connections between technical measurements and operational
decisions.

The pipeline successfully identified high-anomaly periods using the composite
anomaly score generated from multiple sensor variability features. Instead of
looking at individual sensor values, combining multiple signals provided a
more complete view of Rover health.

The KPI framework also showed that different metrics answer different
operational questions. Battery health helps understand energy availability,
fault rate reflects system reliability, and anomaly scores help identify
potential maintenance needs.


## Why KPI Definition Matters

One challenge during this week was defining KPIs that are both technically
meaningful and useful for decision-making.

A metric alone does not create value unless it has a clear interpretation and
action. For example, a high fault rate should trigger investigation or
maintenance review, while declining battery health may indicate charging or
battery replacement requirements.

This connects to real-world data analyst work because analysts need to bridge
the gap between raw data and business decisions.


## Next Question

The next step is integrating these automated reports and KPI outputs into a
dashboard environment.

I want to explore how different stakeholders, such as engineers, product
managers, and operations teams, can interact with the same data while focusing
on different KPIs and decisions.