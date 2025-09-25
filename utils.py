from google import genai
from config import Settings
from typing import Optional
from prompt import SYSTEM_PROMPT
import time

# get google_api_key from settings
settings = Settings()
client = genai.Client(api_key=settings.google_api_key)

def support_function(user_prompt:str) -> Optional[str]:
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_prompt)
    model_response = response.text
    return model_response

def make_prompt(user_prompt:str) -> Optional[str]:
    final_prompt = None
    try:
        final_prompt = f"""system_prompt: {SYSTEM_PROMPT}.
        user_prompt: {user_prompt}"""
    except Exception as e:
        raise e
    
    return final_prompt
# Streamed response emulator
def response_generator(response:str):
 
    for word in response.split():
        yield word + " "
        time.sleep(0.05)