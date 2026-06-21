import pandas as pd

# -----------------------------
# Nettoyage des colonnes numériques
# -----------------------------
def clean_numeric(df, col):

    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.replace("€", "", regex=False)
        .str.strip()
    )

    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    return df


# -----------------------------
# Chargement des données Excel
# -----------------------------
def load_data(file):

    # 1. Lecture Excel
    df = pd.read_excel(file)

    # 2. Colonnes numériques à nettoyer
    numeric_cols = [
        "Sales",
        "Profit",
        "Units Sold",
        "COGS",
        "Discounts"
    ]

    # 3. Nettoyage automatique
    for col in numeric_cols:
        if col in df.columns:
            df = clean_numeric(df, col)

    # 4. Conversion date (si existe)
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    return df
