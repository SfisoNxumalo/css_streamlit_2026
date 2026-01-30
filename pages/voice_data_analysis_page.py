import streamlit as st
import pandas as pd
from integration.openai_client import get_openai_client
from integration.gemini_client import get_gemini_client

def show_voice_ui():
    st.title("Natural Language to Pandas Query")
    st.sidebar.header("Profile Options")

    uploaded_file = st.file_uploader(
        "Upload your dataset (CSV or Excel)",
        type=["csv", "xlsx"]
    )

    client = get_openai_client()


    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.divider()
        st.subheader("Ask a question about your data")

        user_request = st.text_input(
            "Natural language query",
            placeholder="e.g. Show rows where age > 30"
        )

        if user_request:

            schema = extract_df_schema(df)

            prompt = f"""
                   Dataset schema:
                   {schema}

                   User request:
                   "{user_request}"
                   """

            with st.spinner("Generating query..."):
                query_string = client.generate_query(prompt)
                st.code(query_string)

        st.divider()

        st.success("Dataset loaded successfully")
        st.dataframe(df)





# We should extract the dataset's schema so that we can provide our LLM with enough context
def extract_df_schema(df: pd.DataFrame):
    return {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "row_count": len(df)
    }