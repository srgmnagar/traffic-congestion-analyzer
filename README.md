# 🚦 Traffic Congestion Prediction using Real-Time Data (TomTom API)

## 📌 Project Overview
This project analyzes and predicts traffic congestion using **real-time traffic data** collected from the **TomTom Traffic API**.  
Data consists of traffic flow readings (current speed, free-flow speed, confidence, etc.) collected approximately every 15 minutes across multiple locations in **Mumbai & Navi Mumbai**.

We apply **data engineering, exploratory analysis, feature engineering**, and **machine learning** to:
- Understand traffic patterns (rush hours, weekends, location-wise trends)
- Detect congestion using derived metrics
- Build predictive models to forecast traffic conditions

---

## ✅ Current Features Implemented
- 📡 **Automated Data Collection** from TomTom API  
- 🗄 **SQLite Database Storage** (`traffic_data.db`)  
- 🔄 **Data Enrichment** with derived fields:
  - `is_weekend` – weekend flag  
  - `is_rush_hour` – rush-hour flag  
  - `congestion_level` – difference between free-flow and current speed  
  - `traffic_ratio` – normalized traffic speed  
  - `speed_drop_percent` – percentage slowdown from free-flow  
- 🧹 **Data Cleaning & Wrangling** (handling outliers, sorting by time, consistency checks)

---

## 🔥 Planned Steps
1. **Data Cleaning & EDA**
   - Analyze congestion patterns
   - Compare rush vs non-rush, weekend vs weekday
   - Identify outliers and evaluate data reliability

2. **Predictive Modeling**
   - Regression (for future speed prediction)
   - Classification (for congestion category prediction)

3. **Real-Time Prediction Pipeline**
   - Integrate trained model to predict upcoming congestion using live API data

4. **Visualization & Deployment**
   - Interactive dashboard (Streamlit / Power BI)
   - Display historical vs predicted traffic trends


## 🛠 Tech Stack
- **Python** – Data Collection, Analysis, ML  
- **SQLite** – Database Storage  
- **Pandas, Matplotlib, Seaborn** – Data Analysis & Visualization  


