def generate_insights(df):

    insights = []

    top_product = df.groupby("Product")["Sales"].sum().idxmax()
    top_country = df.groupby("Country")["Sales"].sum().idxmax()

    total_profit = df["Profit"].sum()
    total_sales = df["Sales"].sum()

    margin = (total_profit / total_sales) * 100 if total_sales else 0

    insights.append(f"Le produit le plus vendu est {top_product}.")
    insights.append(f"Le pays le plus performant est {top_country}.")
    insights.append(f"Le chiffre d'affaires total est {total_sales:,.0f}.")
    insights.append(f"La marge globale est de {margin:.2f}%.")

    # alerte simple
    if margin < 10:
        insights.append("⚠️ Marge faible détectée.")

    return insights
