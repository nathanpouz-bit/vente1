def compute_kpis(df):

    sales = float(df["Sales"].sum())
    profit = float(df["Profit"].sum())
    units = float(df["Units Sold"].sum())

    if sales == 0:
        margin = 0
    else:
        margin = (profit / sales) * 100

    return {
        "sales": sales,
        "profit": profit,
        "units": units,
        "margin": margin
    }
