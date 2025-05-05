import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/annual_aqi_by_state_2018_2024.csv")
    all_states = pd.DataFrame({
        "state": [
            "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
            "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
            "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
            "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
            "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
        ]
    })
    return all_states.merge(df, on="state", how="left")

df = load_data()

st.title("EnviroWatch USA: Air Quality Dashboard")

year = st.sidebar.slider(
    "Select Year",
    int(df["year"].min()),
    int(df["year"].max()),
    int(df["year"].min())
)
df_year = df[df["year"] == year]

fig = px.choropleth(
    df_year,
    locations="state",
    locationmode="USA-states",
    color="avg_aqi",
    scope="usa",
    color_continuous_scale="RdYlGn_r",
    title=f"Average AQI in {year}"
)
fig.update_traces(marker_line_color="white")

st.plotly_chart(fig, use_container_width=True)
