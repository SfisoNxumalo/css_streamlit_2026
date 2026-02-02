import streamlit as st
import pandas as pd
import time

from google.api_core.exceptions import ResourceExhausted, InternalServerError

from integration.ai.gemini_client import get_gemini_client
from integration.speech_recognition.speech_recognition import SpeechRecognition

# I extract the dataset's schema (column names) so that we can provide
# our LLM with context of available columns and their data types
def extract_df_schema(df: pd.DataFrame):
    return {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "row_count": len(df)
    }

def process_user_request(df: pd.DataFrame, schema: dict, user_request: str, audio_value):

    if user_request and audio_value:
        callouts("info", "Text message received. Audio was ignored", 3)

    if audio_value and not user_request:
        with st.spinner("Transcribing..."):
            vr = SpeechRecognition()
            transcription = vr.transcribe(audio_value)

            if transcription and not transcription.startswith("Error:"):
                user_request = transcription
            else:
                callouts("error", transcription, 3)
                user_request = None

    if user_request:
        with st.spinner("Thinking..."):
            client = get_gemini_client()
            prompt = f"""
               Dataset schema (JSON):
                {schema}
        
               User request:
               "{user_request}"
               """
            query_string = client.generate_query(prompt)

            if query_string == "INVALID_QUERY":
                callouts("error", "Could not generate a valid query.", 4)
            else:
                col1, col2 = st.columns([1, 3], vertical_alignment="center")
                col1.info(f"Generated Query: ")
                col2.code(f"df.query('{query_string}')")
                try:
                    with st.spinner("Loading results..."):
                        filtered_df = df.query(query_string)
                        callouts("success", f"Found {len(filtered_df)} results!", 5)
                        st.dataframe(filtered_df)
                except Exception as e:
                    callouts("error", f"Error applying query: {e}", 4)

# Responsible for displaying feedback to user
def callouts(callout_type: str, message: str, seconds:float = 3):
    placeholder = st.empty()

    if callout_type == "error":
        placeholder.error(message)
    elif callout_type == "warning":
        placeholder.warning(message)
    elif callout_type == "success":
        placeholder.success(message)
    elif callout_type == "info":
        placeholder.info(message)

    time.sleep(seconds)
    placeholder.empty()

def analysis_ui():

    try:

        st.title("Natural Language to Pandas Query")
        st.sidebar.header("Profile Options")

        with st.expander("Upload your dataset", expanded=True):
            st.markdown(
                """
            ##### About this project
            This project uses an LLM to convert a user’s natural language into a Pandas `query` for filtering a provided dataset. Just upload a csv/excel file and ask away!

            **A few things to note:**
            - The LLM is not perfect, so occasional errors are expected (Hopefully you experience none😅).
            - For best results, upload a **cleaned dataset** (you can use the *Top Apps dataset* from Day 2).
            - The LLM does not directly inspect the data itself. Instead, it is provided with the dataset’s **schema** (column names and data types) to better understand what queries are valid.
            - You can either type or use the Speech-to-text feature to send your query

            If you discover a cool or improved way to enhance any functionality, feel free to reach out!  
            Alternatively, you’re welcome to submit a PR on  
            👉 [GitHub Repository](https://github.com/SfisoNxumalo/css_streamlit_2026)
            """
            )

            uploaded_file = st.file_uploader(
                "Upload your dataset (CSV or Excel)",
                type=["csv", "xlsx"]
            )

        if uploaded_file is not None:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            #Convert data in columns of type object to lowercase
            object_cols = df.select_dtypes(include="object").columns
            df[object_cols] = df[object_cols].apply(lambda col: col.str.lower())

            callouts("success", "Dataset loaded successfully", 5)

            schema = extract_df_schema(df)

            st.subheader("Ask a question about your data")

            with st.form("my_form", clear_on_submit=True):

                user_request = st.text_input(
                    "Natural language query",
                    placeholder="e.g. Show rows where age is more than 30",
                    key="message",
                    max_chars=200
                )

                audio_value = st.audio_input("Record high quality audio (e.g. Show me users who are 30 years old)",
                                             key="audio")

                submitted = st.form_submit_button("Process", icon="🤖", width="stretch")

                if submitted and (user_request or audio_value):
                    process_user_request(df, schema, user_request, audio_value)

            st.divider()
            st.dataframe(df)

    except ResourceExhausted:
        callouts("warning", "AI is busy. Please try again shortly.", 4)
    except InternalServerError:
        callouts("error", "AI service is unavailable.", 4)
    except RuntimeError:
        callouts("error", "Unexpected error occurred.", 4)
    except Exception:
        callouts("error", "We experienced an error trying to process the request", 4)
