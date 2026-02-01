import streamlit as st
from openai import OpenAI
from integration.ai.config.ai_config import OPENAI_MODEL, SYSTEM_PROMPT

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=st.secrets["OPENAI_API_KEY"]
        )

    def generate_query(self, user_prompt):
        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()

@st.cache_resource
def get_openai_client() -> OpenAIClient:
    return OpenAIClient()