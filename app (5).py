
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Revenue Dashboard", layout="wide")

st.title("Revenue Dashboard")

uploaded_file = st.file_uploader("Upload Sample_Dataset.xlsx", type=["xlsx"])

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    col1,col2,col3,col4 = st.columns(4)

    col1.metric("Revenue", int(df["Revenue"].sum()))
    col2.metric("Amount", int(df["Amount"].sum()))
    col3.metric("Transactions", len(df))
    col4.metric("Average Revenue", round(df["Revenue"].mean(),2))

    st.subheader("Course Wise Revenue")

    fig,ax=plt.subplots()

    df.groupby("Course")["Revenue"].sum().plot(kind="bar",ax=ax)

    st.pyplot(fig)

    st.subheader("Payment Status")

    fig2,ax2=plt.subplots()

    df["Payment_Status"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax2
    )

    ax2.set_ylabel("")

    st.pyplot(fig2)

    st.subheader("City Wise Revenue")

    fig3,ax3=plt.subplots()

    df.groupby("City")["Revenue"].sum().plot(kind="bar",ax=ax3)

    st.pyplot(fig3)

    st.success("Dashboard Loaded Successfully")
