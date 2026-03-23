# AI Security Agent

This project is a Python tool that automatically finds and analyzes security vulnerabilities (CVEs). 

It gets data from the NIST National Vulnerability Database and uses the Llama 3.3 AI model (via Groq) to explain risks and severity.

## Main Features
- **Auto-Fetch:** Downloads the latest security flaws from the NIST API.
- **AI Analysis:** Uses AI to summarize what the vulnerability does and how bad it is.
- **Save to File:** Saves all analysis into a `findings.json` file.

## Tech Stack
- **Language:** Python 3.13
- **AI Model:** Llama 3.3 (Groq API)
- **Data Source:** NIST NVD API
- **Libraries:** `requests`, `python-dotenv`, `groq`

## Project Structure
- `main.py`: The main script that runs the whole process.
- `tools.py`: Handles downloading data and saving files.
- `llm_agent.py`: Sends the data to the AI.
- `prompts.py`: Contains the instructions for the AI.
- `.env`: Groq API key
