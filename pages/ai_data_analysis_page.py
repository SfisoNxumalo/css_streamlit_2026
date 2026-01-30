import streamlit as st

def show_ai_ui():
    st.title("Natural Language to Pandas Query")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Dr. Jane Doe"
    field = "Astrophysics"
    institution = "University of Science"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")