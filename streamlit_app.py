import streamlit as st

from data_loader import load_data
from kpis import compute_kpis
from analytics import *
from insights import generate_insights
from charts import bar, line, pie

st.set_page_config(layout="wide")

st.title("📊 Sales AI Dashboard")

file = st.file_uploader("Upload Excel", type=["xlsx"])

if file:

    df = load_data(file)

    # KPI
    kpis = compute_kpis(df)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Sales", f"{kpis['sales']:,.0f}")
    c2.metric("Profit", f"{kpis['profit']:,.0f}")
    c3.metric("Units", f"{kpis['units']:,.0f}")
    c4.metric("Margin %", f"{kpis['margin']:.2f}")

    st.divider()

    # INSIGHTS
    st.subheader("💡 Insights automatiques")

    for i in generate_insights(df):
        st.write("•", i)

    st.divider()

    # GRAPHIQUES

    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            bar(sales_by_country(df), "Country", "Sales", "Sales by Country"),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            pie(profit_by_product(df), "Product", "Profit", "Profit by Product"),
            use_container_width=True
        )

    st.plotly_chart(
        line(monthly_trend(df), "Date", "Sales", "Sales Trend")
    )

    st.dataframe(df)
