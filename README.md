# Natural Language to Pandas Query

This Streamlit app lets you ask questions about your dataset in plain English and converts them into Pandas queries to filter your data using AI.  

## Features
- Convert natural language to Pandas queries using an LLM (Gemini/OpenAI).  
- Supports both **text input** and **voice input**.  
- Provides feedback on generated queries and shows filtered results instantly.  
- Works with **uploaded CSV or Excel datasets**.  

## How to Use
1. Upload your dataset (CSV or Excel).  
2. Ask a question in plain English or record your voice.  
3. The app generates a Pandas query and displays the filtered data.  

**Tips:**  
- Upload a **cleaned dataset** for best results  
- The LLM uses the **dataset schema** (columns and types) for context, so queries may not always be perfect.  


## Project Structure
```
project/
│── app.py                  # Main entry point of the Streamlit application
│── requirements.txt        # List of all Python dependencies needed to run the project
│── integration/            # Integration of external libraries (AI and Speech to Text)
│── pages/                  # Streamlit UI
│── .streamlit/
│    └── secrets.toml
```

## Dependencies
- Python 3.9+  
- Streamlit  
- Pandas  
- Gemini/OpenAI Python SDK (or whichever LLM you’re using)  
- openpyxl (for Excel support)  

## How to run

1. Install Libraries:
```pip install -r requirements.txt```

2. Create a file and add your API key:
File: .streamlit/secrets.toml
```GEMINI_API_KEY = "your_key_here"```

3. Run app:
```streamlit run app.py```
