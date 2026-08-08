# Week 8 Internship Retrospective

**Intern:** Ziqing Yang (Clover)  
**Role:** Data Analyst Intern  
**Program:** InGen Dynamics 8-Week Remote Internship

## Most Surprising Finding

The most surprising result was that no single Aido Rover feature dominated the
Random Forest model. Battery rolling mean ranked first with an importance of
0.0706, but the remaining top features had very similar scores.

This showed that physical robot health is a multi-sensor condition. Battery,
LiDAR, rate-of-change, and wheel-torque frequency information must be considered
together.

## Most Important Data Quality Issue

The most important data quality challenge was missing or unstable sensor data.
GPS dropout, LiDAR saturation, and wheel-torque noise could produce misleading
results if they were not identified before analysis.

This reinforced the importance of completing a data quality report before
running statistical tests or machine learning models.

## Most Useful FiberHome Experience

The most useful skill transferred from my FiberHome computer vision internship
was the discipline of testing and validating data before model evaluation.

In computer vision, preprocessing quality directly affects model performance.
The same principle applied to time-series sensor data. Rolling statistics,
rate-of-change features, and FFT features were only meaningful after the raw
data had been checked and cleaned.

## Skills Developed

During the internship, I improved my skills in:

- Python and pandas
- Data quality validation
- Exploratory data analysis
- Statistical testing
- Clustering and segmentation
- Feature engineering
- Random Forest modeling
- KPI design
- Automated reporting
- Dashboard development
- GitHub project organization
- Business communication

## Final Reflection

The project showed me that a data analyst's role is not only to calculate
metrics. The analyst must connect data quality, statistical evidence, technical
outputs, and business decisions.

The strongest final outcome was the creation of an end-to-end workflow that
transformed raw synthetic telemetry into documented findings, KPIs, automated
reports, and dashboard-ready outputs.