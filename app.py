import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    # 1) Load ONLY your cleaned AQI file
    raw = pd.read_csv("data/annual_aqi_by_state_2018_2024.csv")
    raw["year"] = raw["year"].astype(int)    # ensure int

    # 2) Build a master list of states
    all_states = pd.DataFrame({
        "state": [
            "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
            "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
            "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
            "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
            "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
        ]
    })

    # 3) Merge so you get all states (with NaN avg_aqi where missing)
    merged = all_states.merge(raw, on="state", how="left")
    return merged

df = load_data()

st.title("EnviroWatch USA: Air Quality Dashboard")

# ---- slider with fixed bounds ----
year = st.sidebar.slider(
    "Select Year",
    2018,   # min
    2024,   # max
    2018    # default
)

# filter after the slider
df_year = df[df["year"] == year]

fig = px.choropleth(
    df_year,
    locations="state",
    locationmode="USA-states",
    color="avg_aqi",
    scope="usa",
    color_continuous_scale="RdYlGn_r",
    title=f"Average AQI by State ({year})"
)
fig.update_traces(marker_line_color="white")

st.plotly_chart(fig, use_container_width=True)
