import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    # 1. Load your cleaned AQI data
    df = pd.read_csv("data/avg_aqi_by_state.csv")
    # 2. Ensure you have one row per state per year (or, if only one year, merge against all states)
    all_states = pd.DataFrame({
        "state":[
          "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
          "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
          "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
          "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
          "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
        ]
    })
    # Left-merge so missing states show as NaN
    return all_states.merge(df, on="state", how="left")

df = load_data()

st.title("EnviroWatch USA: Air Quality Dashboard")

# If you have multiple years in your CSV, you can add a slider here.
# Otherwise you can skip this block.
if "year" in df.columns:
    year = st.sidebar.slider(
        "Select Year",
        int(df["year"].min()),
        int(df["year"].max()),
        int(df["year"].min())
    )
    df = df[df["year"] == year]

# Create the choropleth
fig = px.choropleth(
    df,
    locations='state',
    locationmode='USA-states',
    color='avg_aqi',
    scope='usa',
    color_continuous_scale='RdYlGn_r',
    title="Average AQI by State"
)
fig.update_traces(marker_line_color="white")

st.plotly_chart(fig, use_container_width=True)
