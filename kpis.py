def compute_kpis(df):

    sales = df["Sales"].sum()
    profit = df["Profit"].sum()
    units = df["Units Sold"].sum()

    margin = (profit / sales * 100) if sales else 0

    return {
        "sales": sales,
        "profit": profit,
        "units": units,
        "margin": margin
    }
