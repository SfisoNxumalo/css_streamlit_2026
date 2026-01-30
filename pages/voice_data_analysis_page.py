import streamlit as st
import pandas as pd

def show_voice_ui():
    st.title("Natural Language to Pandas Query")
    st.sidebar.header("Profile Options")

    uploaded_file = st.file_uploader(
        "Upload your dataset (CSV or Excel)",
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Dataset loaded successfully")
        st.dataframe(df)