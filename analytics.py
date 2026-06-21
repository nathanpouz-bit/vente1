def sales_by_country(df):
    return df.groupby("Country")["Sales"].sum().reset_index()


def sales_by_product(df):
    return df.groupby("Product")["Sales"].sum().reset_index()


def profit_by_product(df):
    return df.groupby("Product")["Profit"].sum().reset_index()


def sales_by_segment(df):
    return df.groupby("Segment")["Sales"].sum().reset_index()


def monthly_trend(df):
    return df.groupby("Date")["Sales"].sum().reset_index()
