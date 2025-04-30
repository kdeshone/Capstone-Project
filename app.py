import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("data/avg_aqi_by_state.csv")  # Replace with your file path

df = load_data()

st.title("EnviroWatch USA: Air Quality Dashboard")

fig = px.choropleth(
    df,
    locations='state',
    locationmode='USA-states',
    color='avg_aqi',
    scope='usa',
    color_continuous_scale='RdYlGn_r',
    title='Average AQI by State'
)

st.plotly_chart(fig, use_container_width=True)
