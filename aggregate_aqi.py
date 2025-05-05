#!/usr/bin/env python3
import os
import zipfile
import pandas as pd

with zipfile.ZipFile("data/raw/annual_aqi_by_county_2018.zip") as z:
    csv_name = next(n for n in z.namelist() if n.endswith(".csv"))
    df = pd.read_csv(z.open(csv_name), nrows=0)
print("Columns in county file:", df.columns.tolist())

# 1) ensure folders exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data", exist_ok=True)

# 2) years to process
years = list(range(2018, 2025))
records = []

# 3) loop over downloaded ZIP files in data/raw/
for year in years:
    zip_path = f"data/raw/annual_aqi_by_county_{year}.zip"
    if not os.path.isfile(zip_path):
        print(f"⚠️  Missing {zip_path}  – please download it into data/raw/")
        continue

    # extract and read
    with zipfile.ZipFile(zip_path) as z:
        csv_name = next(n for n in z.namelist() if n.endswith(".csv"))
        df_county = pd.read_csv(z.open(csv_name))

    # aggregate county → state (by FIPS code)
    df_state = (
        df_county
        .groupby("State Code", as_index=False)["AQI"]
        .mean()
        .rename(columns={"State Code": "fips", "AQI": "avg_aqi"})
    )
    df_state["year"] = year
    records.append(df_state)

# 4) combine all years
df_aqi = pd.concat(records, ignore_index=True)

# 5) map FIPS → USPS abbreviation
fips_map = {
    '01':'AL','02':'AK','04':'AZ','05':'AR','06':'CA','08':'CO','09':'CT','10':'DE',
    '12':'FL','13':'GA','15':'HI','16':'ID','17':'IL','18':'IN','19':'IA','20':'KS',
    '21':'KY','22':'LA','23':'ME','24':'MD','25':'MA','26':'MI','27':'MN','28':'MS',
    '29':'MO','30':'MT','31':'NE','32':'NV','33':'NH','34':'NJ','35':'NM','36':'NY',
    '37':'NC','38':'ND','39':'OH','40':'OK','41':'OR','42':'PA','44':'RI','45':'SC',
    '46':'SD','47':'TN','48':'TX','49':'UT','50':'VT','51':'VA','53':'WA','54':'WV',
    '55':'WI','56':'WY'
}
df_aqi["state"] = df_aqi["fips"].astype(str).str.zfill(2).map(fips_map)

# 6) final selection & save
df_aqi = df_aqi[["state", "year", "avg_aqi"]]
out_path = "data/annual_aqi_by_state_2018_2024.csv"
df_aqi.to_csv(out_path, index=False)

print(f"✔️  Wrote: {out_path}")
