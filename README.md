# AI-Driven Security Intelligence Aggregator

This project is a backend service developed in Python that aggregates security information from the NIST NVD API and uses a Large Language Model (LLM) to extract insights.

## 1. AI Agent & Prompt Design
The agent processes the ingested text using the **Llama 3.3** model (via **Groq API**) to extract:
- **Key security topics:** Malware, Phishing, Ransomware, Zero-days, etc.
- **Severity level:** Low, Medium, High, or Critical.
- **Summary:** A short AI-generated technical overview.

### Prompt Structure
The system uses a structured prompt to ensure the LLM returns a strict JSON format for automated processing.

## 2. MCP-Style Tools
The agent implements two core tools for the workflow:
- `fetchSecurityData()`: Retrieves data from the public NIST source.
- `storeFinding()`: Stores the processed AI results into a local `findings.json` file.
