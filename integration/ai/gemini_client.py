import streamlit as st
import google.generativeai as genai
from integration.config.ai_config import GEMINI_MODEL, SYSTEM_PROMPT


class GeminiClient:
    def __init__(self):
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel(GEMINI_MODEL)

    def generate_query(self, user_prompt: str) -> str:
        prompt = f"""
        {SYSTEM_PROMPT}
        
        User request:
        {user_prompt}
        """
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0,
                "max_output_tokens": 200
            }
        )

        return response.text.strip()

@st.cache_resource
def get_gemini_client() -> GeminiClient:
    return GeminiClient()
