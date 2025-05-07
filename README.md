# EnviroWatch USA

EnviroWatch USA is an interactive data visualization dashboard built with Streamlit that allows users to explore trends in air quality and carbon emissions across U.S. states from 2018 to 2024.

## 🌎 Overview
This app enables comparison and trend analysis using two key environmental indicators:
- **Air Quality Index (AQI)**: Sourced from EPA’s annual AQI reports by state.
- **CO₂ Emissions (tons)**: Derived from EPA’s FLIGHT tool, aggregated by state and year.

Users can filter by year, choose a specific state, and switch between metrics to view:
- A choropleth map of the selected metric
- A line chart showing that metric’s trend over time for a selected state

## 📁 Project Structure
```
Capstone-Project/
├── app.py                     # Streamlit application
├── data/
│   ├── annual_aqi_by_state_2018_2024.csv
│   ├── processed_state_co2.csv
├── scripts/                  # Processing scripts (optional)
│   └── process_co2.py
├── README.md
└── requirements.txt
```

## 🧪 How to Run the App
1. Clone this repository:
```bash
git clone https://github.com/your-username/Capstone-Project.git
cd Capstone-Project
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Launch the Streamlit app:
```bash
streamlit run app.py
```

## 📊 Data Sources
- [EPA AQI Reports](https://www.epa.gov/air-trends)
- [EPA FLIGHT Tool](https://ghgdata.epa.gov/ghgp/main.do)

## ✅ Features
- Dynamic year slider and state filter
- Metric toggle between AQI and CO₂
- Auto-zoom and state abbreviation labels on maps
- State-level line charts over time

## 📌 Notes
- Emissions data were cleaned and transformed from raw EPA Excel files.
- AQI data were averaged across counties to the state level.

## 🎥 Video Demo
*To be submitted separately.*

## 📄 License
MIT License — see [LICENSE](LICENSE) for details.

## 👥 Team
- Your Name Here
- Contact: your.email@example.com
