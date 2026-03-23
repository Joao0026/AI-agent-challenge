import os
import json
from groq import Groq
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, build_user_prompt

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def analyze_with_llm(cve_id, description):
    prompt_text = build_user_prompt(cve_id, description)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text}
        ],
        response_format={"type": "json_object"},
        timeout=10.0
    )

    result_text = response.choices[0].message.content
    return json.loads(result_text)