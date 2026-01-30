import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Researcher Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Go to:",
    ["AI Data Analysis", "Developer"],
)

if menu == "AI Data Analysis":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Jane Doe"
    field = "Astrophysics"
    institution = "University of Science"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")


elif menu == "Developer":
    # Add a contact section
    st.header("Contact Information")
    email = "jane.doe@example.com"
    st.write(f"You can reach me at {email}.")

    st.image(
        "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
        caption="Nature (Pixabay)")