import time
from tools import fetchSecurityData, storeFinding
from llm_agent import analyze_with_llm

def start_app():
    print("-- CVE Security Agent Starting --")
    
    cve_list = fetchSecurityData()
    print(f"[*] Found {len(cve_list)} items.\n")

    for item in cve_list:
        cve_id = item["cve_id"]
        print(f"[>] Analyzing {cve_id}...")

        ai_result = analyze_with_llm(cve_id, item["description"])

        final_report = {
            "cve_id": cve_id,
            "original_desc": item["description"],
            "ai_analysis": ai_result
        }
        
        storeFinding(final_report)
        print(f"    - Done: {cve_id} saved.")
        
        time.sleep(1) 

    print("\n[!] All tasks finished. Check findings.json")

if __name__ == "__main__":
    start_app()