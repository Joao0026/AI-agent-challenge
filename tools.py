import json
import requests

def fetchSecurityData():
    # URL for NIST API (v2.0)
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=5"
    print(f"[*] Fetching data from: {url}")
    
    # Simple request without error handling
    response = requests.get(url, timeout=30)
    data = response.json()
    
    parsed_list = []
    vulnerabilities = data.get("vulnerabilities", [])

    for item in vulnerabilities:
        cve_info = item.get("cve", {})
        
        description = "No description found"
        descriptions = cve_info.get("descriptions", [])
        
        for desc in descriptions:
            if desc.get("lang") == "en":
                description = desc.get("value")
                break
        
        parsed_list.append({
            "cve_id": cve_info.get("id"),
            "description": description
        })
        
    return parsed_list

def storeFinding(new_result):
    filename = "findings.json"
    
    f = open(filename, "r")
    current_data = json.load(f)
    f.close()

    current_data.append(new_result)
    
    f = open(filename, "w")
    json.dump(current_data, f, indent=2)
    f.close()