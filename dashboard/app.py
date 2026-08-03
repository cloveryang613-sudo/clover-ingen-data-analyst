import streamlit as st
import pandas as pd


st.title(
    "InGen Dynamics Executive Dashboard"
)


st.header(
    "Aido Rover Health Overview"
)


# Load KPI data

kpi = pd.read_csv(
    "data/rover_kpi_summary.csv"
)


# create four cards

col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Battery SOC",
    round(
        kpi["mean_battery_soc"][0],
        2
    )
)


col2.metric(
    "Fault Rate",
    str(
        round(
            kpi["fault_rate"][0]*100,
            2
        )
    ) + "%"
)


col3.metric(
    "LiDAR Distance",
    round(
        kpi["mean_lidar_distance"][0],
        2
    )
)


col4.metric(
    "Anomaly Count",
    int(
        kpi["high_risk_count"][0]
    )
)


st.header(
    "Rover Feature Importance"
)


importance = pd.read_csv(
    "data/rover_feature_importance.csv"
)


st.bar_chart(
    importance.set_index(
        "feature"
    )
)