🚦 Traffic Congestion Prediction using Real-Time Data (TomTom API)
📌 Project Overview
This project aims to analyze and predict traffic congestion using real-time data collected from the TomTom Traffic API.
The dataset consists of traffic flow readings (current speed, free-flow speed, confidence, etc.) collected every 15 minutes across multiple locations in Mumbai & Navi Mumbai.

We combine data engineering, exploratory analysis, feature engineering, and machine learning to:

Understand traffic patterns (rush hours, weekends, location-wise trends)

Detect congestion patterns using derived metrics

Build a predictive model to forecast traffic conditions

✅ Current Features Implemented
📡 Automated Data Collection from TomTom API

🗄 SQLite Database Storage (traffic_data.db)

🔄 Data Enrichment with derived fields:

is_weekend – weekend flag

is_rush_hour – rush-hour flag

congestion_level – free-flow vs current speed difference

traffic_ratio – normalized speed measure

speed_drop_percent – percentage slowdown

🧹 Data Cleaning & Wrangling (handling outliers, sorting, consistency checks)

🔥 Planned Steps
Data Cleaning & EDA

Analyze congestion patterns

Compare rush vs non-rush, weekend vs weekday

Identify outliers and data reliability

Feature Engineering

Add lag features, rolling averages

Encode time-of-day segments (hour_bin), location clusters

Predictive Modeling

Regression (for speed prediction)

Classification (for congestion category)

Real-Time Prediction Pipeline

Integrate model to predict upcoming congestion using live API data

Visualization & Deployment

Interactive dashboard (Streamlit / Power BI)

Historical vs predicted traffic trends

🛠 Tech Stack
Python – Data Collection, Analysis, ML

SQLite – Database Storage

Pandas, Matplotlib, Seaborn – Data Analysis & Visualization
