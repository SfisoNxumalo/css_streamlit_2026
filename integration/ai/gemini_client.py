import streamlit as st
import google.generativeai as genai
from google.api_core.exceptions import InternalServerError, ResourceExhausted

from integration.ai.config.ai_config import GEMINI_MODEL, SYSTEM_PROMPT

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

        try:

            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0,
                    "max_output_tokens": 200
                }
            )

            if not response or not response.text:
                raise ValueError("Empty response from AI service")

            return response.text.strip()

        except ResourceExhausted as e:
            # Rate limit / quota exceeded
            raise ResourceExhausted(
                "AI rate limit exceeded. Please retry later."
            ) from e

        except InternalServerError as e:
            # Gemini internal failure
            raise InternalServerError(
                "AI service encountered an internal error."
            ) from e

        except Exception as e:
            # Unexpected failure
            raise RuntimeError(
                f"Unexpected AI error: {str(e)}"
            ) from e

@st.cache_resource
def get_gemini_client() -> GeminiClient:
    return GeminiClient()
