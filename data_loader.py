from config.columns import REQUIRED_COLUMNS

import pandas as pd

REQUIRED_COLUMNS = [
    "Segment", "Country", "Product", "Discount Band",
    "Units Sold", "Manufacturing Price", "Sale Price",
    "Gross Sales", "Discounts", "Sales", "COGS",
    "Profit", "Date", "Month Number", "Month Name", "Year"
]

def load_data(file):
    df = pd.read_excel(file)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Colonnes manquantes: {missing}")

    df["Date"] = pd.to_datetime(df["Date"])
    return df
