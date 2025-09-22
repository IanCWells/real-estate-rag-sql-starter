from homeharvest import scrape_property
from datetime import datetime
import pandas as pd
import sqlite3
import json

#Function to clean data
def clean_dataframe(df):
    for col in df.columns:
        df[col] = df[col].apply(
            lambda x: json.dumps(x) if isinstance(x, (list, dict)) else x
        )
    return df

#Scrapes Properties
properties = scrape_property(
  location="Costa Mesa, CA",
  listing_type="for_sale",
  property_type=['multi_family']
)

properties = clean_dataframe(properties)
# connect (creates file if not exists)
conn = sqlite3.connect("properties.db")
# write dataframe to SQL
properties.to_sql("properties", conn, if_exists="replace", index=False)

conn.close()
