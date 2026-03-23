SYSTEM_PROMPT = """
You are a security assistant. 
Analyze the description and provide:
1. topics: list of themes (e.g., malware, exploit)
2. severity: Low, Medium, High, or Critical
3. summary: one short sentence

Return ONLY a JSON object.
"""

def build_user_prompt(cve_id, description):
    return f"""
Analyze this vulnerability and return JSON:
ID: {cve_id}
Description: {description}

JSON structure:
{{
  "topics": [],
  "severity": "",
  "summary": ""
}}
"""