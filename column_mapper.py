import pandas as pd

# Dictionnaire d'équivalences (très important)
COLUMN_SYNONYMS = {
    "Sales": ["sales", "revenue", "ca", "chiffre d'affaires", "turnover"],
    "Profit": ["profit", "benefit", "net income", "marge"],
    "Units Sold": ["units sold", "quantity", "qty", "volume"],
    "Country": ["country", "pays", "nation"],
    "Product": ["product", "item", "produit"],
    "Segment": ["segment", "customer segment"],
    "Discounts": ["discount", "reduction", "remise"]
}


def normalize(col):
    return col.strip().lower()


def detect_column(df, target):
    """Trouve la meilleure colonne correspondant à un champ métier"""
    synonyms = COLUMN_SYNONYMS.get(target, [])
    cols = df.columns

    for col in cols:
        for syn in synonyms:
            if syn in normalize(col):
                return col

    return None


def map_columns(df):
    """Crée un mapping standard → fichier utilisateur"""

    mapping = {}

    for standard_name in COLUMN_SYNONYMS.keys():
        detected = detect_column(df, standard_name)
        if detected:
            mapping[standard_name] = detected

    return mapping


def apply_mapping(df, mapping):
    """Renomme les colonnes vers un format standard"""

    df = df.copy()

    rename_dict = {v: k for k, v in mapping.items()}

    df = df.rename(columns=rename_dict)

    return df, rename_dict
