from config.columns import REQUIRED_COLUMNS

import pandas as pd

REQUIRED_COLUMNS = [
    "Segment", "Country", "Product", "Discount Band",
    "Units Sold", "Manufacturing Price", "Sale Price",
    "Gross Sales", "Discounts", "Sales", "COGS",
    "Profit", "Date", "Month Number", "Month Name", "Year"
]

def validate_columns(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]

    if missing:
        raise ValueError(
            f"Colonnes manquantes dans ton fichier Excel : {missing}"
        )
import pandas as pd
from column_mapper import map_columns, apply_mapping


def load_data(file):

    df = pd.read_excel(file)

    # 1. détection automatique
    mapping = map_columns(df)

    # 2. appliquer mapping
    df, rename_dict = apply_mapping(df, mapping)

    # 3. vérifier les colonnes critiques
    required = ["Sales", "Profit", "Country", "Product"]

    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(
            f"Impossible de détecter ces colonnes : {missing}"
        )

    # 4. conversion date si possible
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    return df
