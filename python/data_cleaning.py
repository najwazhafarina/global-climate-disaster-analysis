import pandas as pd


df = pd.read_excel("data/raw/emdat_disasters.xlsx")

print("Original dataset shape:")
print(df.shape)


columns_needed = [
    "DisNo.",
    "Country",
    "Region",
    "Subregion",
    "Disaster Type",
    "Disaster Subtype",
    "Start Year",
    "Start Month",
    "Total Deaths",
    "No. Affected",
    "Total Affected",
    "Total Damage ('000 US$)",
    "Latitude",
    "Longitude"
]

df = df[columns_needed]

print("\nAfter selecting columns:")
print(df.shape)


df["Total Deaths"] = df["Total Deaths"].fillna(0)
df["Total Affected"] = df["Total Affected"].fillna(0)
df["Total Damage ('000 US$)"] = df["Total Damage ('000 US$)"].fillna(0)

df = df.dropna(subset=["Country", "Start Year"])


df["Start Year"] = df["Start Year"].astype(int)
df["Total Deaths"] = df["Total Deaths"].astype(int)
df["Total Affected"] = df["Total Affected"].astype(int)


df = df.rename(columns={
    "DisNo.": "disaster_id",
    "Country": "country",
    "Region": "region",
    "Subregion": "subregion",
    "Disaster Type": "disaster_type",
    "Disaster Subtype": "disaster_subtype",
    "Start Year": "year",
    "Start Month": "month",
    "Total Deaths": "total_deaths",
    "No. Affected": "affected_people",
    "Total Affected": "total_affected",
    "Total Damage ('000 US$)": "total_damage_usd",
    "Latitude": "latitude",
    "Longitude": "longitude"
})


df.to_csv("data/cleaned/disasters_clean.csv", index=False)

print("\nClean dataset saved!")
print("Final dataset shape:")
print(df.shape)
