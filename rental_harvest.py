import json
import sqlite3
from homeharvest import scrape_property

# define cleaner
def clean_dataframe(df):
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x
        )
    return df   # must be inside the function

# scrape rentals
rentals = scrape_property(
    location="Costa Mesa, CA",
    listing_type="for_rent",
)

print("Raw columns:", rentals.columns.tolist())


# clean + save to sqlite
rentals = clean_dataframe(rentals)

conn = sqlite3.connect("rentals.db")

rentals.to_sql("rentals", conn, if_exists="replace", index=False)
conn.close()

