import pandas as pd

# ==============================
# 1. LOAD DATASET
# ==============================

df = pd.read_excel("data/raw/emdat_disasters.xlsx")

print("Original dataset shape:")
print(df.shape)

# ==============================
# 2. SELECT IMPORTANT COLUMNS
# ==============================

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

# ==============================
# 3. HANDLE MISSING VALUES
# ==============================

df["Total Deaths"] = df["Total Deaths"].fillna(0)
df["Total Affected"] = df["Total Affected"].fillna(0)
df["Total Damage ('000 US$)"] = df["Total Damage ('000 US$)"].fillna(0)

# drop rows yang tidak punya country atau year
df = df.dropna(subset=["Country", "Start Year"])

# ==============================
# 4. DATA TYPE CLEANING
# ==============================

df["Start Year"] = df["Start Year"].astype(int)
df["Total Deaths"] = df["Total Deaths"].astype(int)
df["Total Affected"] = df["Total Affected"].astype(int)

# ==============================
# 5. RENAME COLUMNS (SQL FRIENDLY)
# ==============================

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

# ==============================
# 6. SAVE CLEAN DATASET
# ==============================

df.to_csv("data/cleaned/disasters_clean.csv", index=False)

print("\nClean dataset saved!")
print("Final dataset shape:")
print(df.shape)