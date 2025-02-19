import http.client
import urllib.parse
import json

# API Connection Setup
conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    'Content-Type': 'application/json'
}

# Function to fetch defect details
def get_defect_details(defect_id):
    """Fetch defect details from API and return JSON response."""
    try:
        conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/{defect_id}", payload, headers)
        res = conn.getresponse()
        if res.status != 200:
            print(f"Error fetching defect {defect_id}: HTTP {res.status}")
            return None
        data = res.read()
        return json.loads(data.decode("utf-8"))
    except Exception as e:
        print(f"Exception fetching defect {defect_id}: {e}")
        return None

# Function to classify defects based on validation
def classify_defects(defect_ids, release_id):
    """Classify defects as validated or not based on API response."""
    validated = []
    not_validated = []

    for defect_id in defect_ids:
        defect_data = get_defect_details(defect_id)
        if not defect_data or "workItems" not in defect_data:
            not_validated.append(defect_id)
            continue

        is_validated = any(
            "validatedIn" in item and any(v['id'] == release_id for v in item['validatedIn'].get('value', []))
            for item in defect_data['workItems']
        )

        if is_validated:
            validated.append(defect_id)
        else:
            not_validated.append(defect_id)

    return validated, not_validated

# Fetch defect list based on query
def get_defect_list():
    """Fetch list of defects matching query."""
    query = (
        "type:defect AND NOT validatedIn.KEY:LCS-1079215"
    )
    encoded_query = urllib.parse.quote(query)
    url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"

    try:
        conn.request("GET", url, payload, headers)
        res = conn.getresponse()
        if res.status != 200:
            print(f"Error fetching defect list: HTTP {res.status}")
            return []

        data = json.loads(res.read().decode("utf-8"))
        return [item['id'][11:] for item in data.get('data', []) if item['type'] == "workitems"]
    except Exception as e:
        print(f"Exception fetching defect list: {e}")
        return []

# Main Execution
if __name__ == "__main__":
    defect_ids = get_defect_list()
    if not defect_ids:
        print("No defects found.")
    else:
        validated, not_validated = classify_defects(defect_ids, "LCS-1079215")

        print("\nValidated Defects:")
        print(validated if validated else "None")

        print("\nNot Validated Defects:")
        print(not_validated if not_validated else "None")
