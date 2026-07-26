# Week 5 CV-Informed Feature Analysis Report

**Intern:** Ziqing Yang (Clover)  
**Role:** Data Analyst Intern  
**Company:** InGen Dynamics Inc.  
**Week:** Week 5  
**Product Anchors:** Aido Rover and Fari  

---

## 1. Executive Summary

This analysis applied computer vision feature extraction concepts to time-series
sensor data from the Aido Rover and interaction data from Fari.

For the Aido Rover, the Random Forest model found that
`battery_rolling_mean` was the highest-ranked derived feature, with an
importance score of 0.0706. It was followed closely by
`battery_rolling_std` with an importance of 0.0703.

However, the top ten Rover feature importance scores were relatively close,
ranging from approximately 0.064 to 0.071. This indicates that Rover operating
status is predicted through the combined contribution of temporal statistics,
rates of change, and frequency-domain wheel-torque features rather than one
dominant feature.

For Fari, `response_length` was the strongest predictor of interaction quality,
with an importance score of 0.3847. `sentiment_score` ranked second with an
importance score of 0.2955. The Fari Random Forest model achieved approximately
88% test accuracy.

Overall, the analysis demonstrates that computer vision feature extraction
principles can be transferred to both robot sensor signals and human-robot
interaction data.

---

## 2. Data Quality Assessment

Before feature extraction, the Aido Rover dataset was checked for row count,
column names, data types, missing values, duplicate records, physical range
violations, and status-label distribution.

The dataset included timestamp, GPS, LiDAR, battery, wheel-torque, temperature,
and status information. Missing numeric sensor values were handled using
interpolation because the observations form a continuous time series.

The feature engineering process used a rolling window of 20 timesteps. As a
result, the first 19 rows of rolling features contained missing values. These
rows were removed before model training.

The Fari dataset contained 2,000 synthetic interaction sessions. It included
five numeric features and one binary quality label. The high- and low-quality
classes were balanced, and no missing values were introduced.

---

## 3. Feature Extraction Methodology

The Aido Rover analysis transformed raw sensor values into derived features
that describe local behavior, instability, transitions, and frequency patterns.

### 3.1 Rolling Mean

Rolling means were calculated for battery state of charge and LiDAR distance
using a window of 20 timesteps.

The rolling mean represents the local operating level of a sensor. For example,
battery rolling mean describes the average battery level over a short operating
period rather than at one isolated timestep.

### 3.2 Rolling Standard Deviation

Rolling standard deviations were calculated for battery and LiDAR readings.

These features measure short-term sensor instability. Higher rolling standard
deviation indicates that readings are changing more strongly within the local
window.

### 3.3 Rate of Change

First-order differences were calculated for battery and LiDAR readings.
Absolute rate-of-change features were also created to measure the size of each
change regardless of direction.

High rate-of-change values can indicate sudden transitions, unstable movement,
or unusual operating conditions.

### 3.4 FFT Frequency Features

Fast Fourier Transform analysis was applied to the four wheel-torque channels.

For each rolling window, two frequency-domain features were extracted:

- Dominant frequency
- Total spectral power

Dominant frequency identifies the strongest repeated pattern in the torque
signal. Spectral power measures the overall strength of periodic variation and
may reflect vibration or repeated mechanical loading.

### 3.5 Composite Anomaly Score

A composite anomaly score was calculated using the local coefficient of
variation across battery, LiDAR, wheel-torque, and temperature signals.

This score summarizes instability across several sensors. Higher values
represent periods with greater combined sensor variation.

---

## 4. Computer Vision Methodology Connection

The feature engineering methods used in this analysis have direct parallels
with computer vision preprocessing.

Rolling mean is similar to an image smoothing filter. In image processing, a
local filter summarizes nearby pixels. In sensor analysis, a rolling mean
summarizes nearby timesteps.

Rolling standard deviation is similar to a local texture descriptor. Smooth
image regions contain low pixel variation, while textured regions and edges
contain greater local variation. Similarly, unstable sensor periods produce
higher rolling standard deviation.

Rate of change is similar to edge detection. Image edges occur where pixel
intensity changes rapidly. Sensor transitions occur where values change rapidly
between consecutive timesteps.

FFT features are comparable to frequency-domain image analysis. Frequency
methods can identify repeating image textures, while torque FFT features
identify repeated mechanical cycles and vibration patterns.

The composite anomaly score is similar to combining several visual feature
maps to identify unusual image regions.

---

## 5. Aido Rover Random Forest Results

A Random Forest classifier was trained using only the derived features. The
dataset was divided using a stratified 70% training, 15% validation, and 15%
testing split.

The ten highest-ranked Rover features were:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | battery_rolling_mean | 0.070588 |
| 2 | battery_rolling_std | 0.070319 |
| 3 | lidar_rolling_mean | 0.067617 |
| 4 | lidar_abs_rate_change | 0.067353 |
| 5 | lidar_rolling_std | 0.067307 |
| 6 | wheel_torque_3_spectral_power | 0.066807 |
| 7 | battery_abs_rate_change | 0.066522 |
| 8 | lidar_rate_of_change | 0.066149 |
| 9 | battery_rate_of_change | 0.065223 |
| 10 | wheel_torque_2_spectral_power | 0.064112 |

Battery rolling mean was the highest-ranked feature, but its importance was only
slightly higher than the other top features.

This result suggests that Rover status is a multi-sensor condition. Battery
level, battery instability, LiDAR behavior, rapid sensor changes, and
wheel-torque frequency patterns all contribute useful predictive information.

The presence of wheel-torque spectral-power features indicates that repeated
mechanical patterns may help distinguish normal, warning, and fault operating
states.

---

## 6. Fari Interaction Feature Analysis

A synthetic Fari dataset with 2,000 interaction sessions was created using the
following features:

- Response length
- Sentiment score
- Topic coherence
- Response latency
- Session duration

A Random Forest classifier was trained to predict whether each interaction was
high or low quality.

The feature importance results were:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | response_length | 0.384714 |
| 2 | sentiment_score | 0.295451 |
| 3 | topic_coherence | 0.156744 |
| 4 | latency_ms | 0.096397 |
| 5 | session_duration | 0.066693 |

The model achieved approximately 88% test accuracy.

Response length was the strongest predictor of interaction quality. This
suggests that responses containing an appropriate amount of information are
more likely to support successful interactions than responses that are too
short or insufficiently detailed.

Sentiment score was the second most important feature. This indicates that the
emotional tone of the interaction provides a strong signal of session quality.

Topic coherence ranked third, showing that remaining focused on the user's
topic also contributes to interaction quality. Latency and session duration
were less influential but still provided useful supporting information.

---

## 7. Platform Comparison

The Aido Rover and Fari models produced different feature importance patterns.

For the Rover model, feature importance was distributed relatively evenly
across temporal, rate-of-change, and frequency-domain measurements. No single
feature dominated the model.

For Fari, the top two features accounted for most of the predictive importance.
Response length and sentiment were substantially more important than latency
and session duration.

This difference reflects the operational purpose of each platform.

Aido Rover health is a physical, multi-sensor condition that requires several
signals to be evaluated together. Fari interaction quality is more strongly
associated with a smaller number of conversational characteristics.

---

## 8. Operational Implications

For the Aido Rover, InGen could use rolling battery statistics, LiDAR changes,
and wheel-torque spectral power as inputs to a fleet-health monitoring system.

These features may support:

- Early warning detection
- Predictive maintenance
- Battery-health monitoring
- Mechanical vibration monitoring
- Identification of unusual operating periods

For Fari, response length, sentiment, and topic coherence could be included in
an interaction-quality score.

These features may support:

- Conversation-quality monitoring
- Identification of low-quality sessions
- Response-generation improvements
- User-experience evaluation
- Product-level KPI reporting

---

## 9. Limitations

The Rover and Fari datasets are synthetic. Their distributions may not fully
represent real-world robot deployments or real human interactions.

The Fari quality label was generated using a predefined synthetic formula.
Therefore, the feature importance results partly reflect the assumptions used
to create that formula.

Random Forest feature importance identifies predictive contribution but does
not establish causation.

The Rover composite anomaly score used a simplified combination of sensor
variability. Future work could use validated PCA loadings or learned anomaly
weights from production data.

The analysis used one rolling-window size of 20 timesteps. Different window
sizes may produce different feature rankings.

---

## 10. Conclusion

The Week 5 analysis successfully transferred computer vision feature extraction
concepts to robot time-series and interaction data.

For the Aido Rover, local averages, local variability, rates of change, and FFT
features jointly contributed to operating-status prediction.

For Fari, response length and sentiment score were the strongest predictors of
interaction quality.

The generated feature rankings provide useful pre-computed outputs for the
Week 6 reporting pipeline and the Week 7 dashboard.