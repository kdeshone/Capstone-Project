import os, zipfile, pandas as pd

os.makedirs("data/raw", exist_ok=True)
os.makedirs("data", exist_ok=True)

years = list(range(2018, 2025))
records = []

for year in years:
    path = f"data/raw/annual_aqi_by_county_{year}.zip"
    if not os.path.isfile(path):
        print(f"⚠ Missing {path}")
        continue

    with zipfile.ZipFile(path) as z:
        csv_name = next(n for n in z.namelist() if n.endswith(".csv"))
        df_county = pd.read_csv(z.open(csv_name), low_memory=False)

    # group by State column, average the Median AQI
    df_state = (
        df_county
        .groupby("State", as_index=False)["Median AQI"]
        .mean()
        .rename(columns={"State": "state", "Median AQI": "avg_aqi"})
    )
    df_state["year"] = year
    records.append(df_state)

# combine and write out
df_aqi = pd.concat(records, ignore_index=True)
df_aqi.to_csv("data/annual_aqi_by_state_2018_2024.csv", index=False)
print("✔ Wrote data/annual_aqi_by_state_2018_2024.csv")
