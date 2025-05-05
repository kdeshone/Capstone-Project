import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    df = pd.read_csv("data/annual_aqi_by_state_2018_2024.csv")

    # 1. Drop any rows where 'year' is missing
    df = df.dropna(subset=["year"])

    # 2. Ensure 'year' is integer
    df["year"] = df["year"].astype(int)

    # 3. (Optional) Merge with full-state list to show missing avg_aqi as blank
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

# Compute slider bounds from the cleaned data
years = df["year"].dropna().astype(int)
min_year, max_year = int(years.min()), int(years.max())

# Sidebar slider
year = st.sidebar.slider(
    "Select Year",
    min_year,
    max_year,
    min_year
)

# Filter for that year
df_year = df[df["year"] == year]

# Build the map
st.title(f"EnviroWatch USA: AQI in {year}")
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
