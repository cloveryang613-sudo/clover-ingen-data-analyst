# Week 5 Data Analyst Log

**Intern:** Ziqing Yang (Clover)  
**Week:** Week 5  
**Focus:** CV-Informed Sensor Feature Analysis  

## What I Analyzed

This week, I applied computer vision feature extraction concepts to Aido Rover
time-series sensor data. I created rolling mean, rolling standard deviation,
rate-of-change, FFT dominant-frequency, spectral-power, and composite anomaly
features. I then trained a Random Forest classifier using only the derived
features to predict normal, warning, and fault status.

I also generated a synthetic dataset containing 2,000 Fari interaction sessions.
The dataset included response length, sentiment, topic coherence, latency, and
session duration. A second Random Forest model was used to predict high- and
low-quality interactions.

## What I Found

For the Aido Rover, battery rolling mean was the highest-ranked feature with an
importance of 0.0706. Battery rolling standard deviation ranked second at
0.0703. However, the top Rover feature scores were very close, showing that
status prediction depends on several complementary sensor patterns.

For Fari, response length was the strongest predictor with an importance of
0.3847, followed by sentiment score at 0.2955. The Fari model achieved
approximately 88% test accuracy.

## FiberHome Connection

The most surprising result was that no single Rover feature strongly dominated
the model. This matched my FiberHome computer vision intuition because image
recognition models usually combine multiple features such as texture, edges,
and frequency patterns rather than relying on one raw input.

## Next Question

My next question is whether the same feature rankings remain stable when the
rolling-window size changes. I also want to investigate whether the highest-ranked
Rover features can support a real-time anomaly alert or fleet-health KPI.