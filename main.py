import streamlit as st
import pandas as pd
import numpy as np
from pages.Voice_data_analysis_page import show_ai_ui
from pages.developer_details_page import show_developer_details

st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Go to:",
    ["Voice Data Analysis", "Developer"],
)

if menu == "Voice Data Analysis":
    show_ai_ui()

elif menu == "Developer":
    show_developer_details()