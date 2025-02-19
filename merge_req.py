import http.client
import urllib.parse
import json

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
  'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiZjQ2ODQyYjctOTI3YTE2ZjMtM2U4ZDc0ZDEtNTk0NjY4ZmEiLCJleHAiOjE3NzA2NjE4MDAsImlhdCI6MTczOTI2NzI2MX0.BEF_nzrN7iAuKVzND_Z5xlxLRDYV1Vy3CXTgZwMPFSgfUnwA_t7BDyIOOU1DgyjfVfXv_O-QkClDdO8FUUei8Wbiy6VWArbGs5_BmwLwBMCJF457xW5hpjqvQtGsVNLAAYb0pFR8tmO-oushWr9RBiqBpEnsQdhtMrDy69EFCW5PZWeeL1USMot2-PdKBYcGW_w1lAPAL4m2IezmUHm2topn853Dq8D_OoFXLNkLJMN2ifIU_M9dQ72vFDo8I6Tx3Fg_L-uTxa6wmr_g5SaYIqmX6tFzkiezW_lV71RjfHTSc1NJAzYCIORHdb2OS8NA-NG-6e-TwWjM3KY65Np0TA',
  'Cookie': 'JSESSIONID=B79D4AC260AEDD5C492C84B188D67761.node1; JSESSIONIDSSO=3CF16C0CA79AF2D3297E0B34F55D2C80'
}

#---------------------------------------------------- populate fixedIn ----------------------------------------------------

def populate_fixedIn(defect_id, release_id):
    print("called")
    defect_id="LCS-961346"
    payload = json.dumps({
         "fixedInRelease": release_id
    })
    headers = {
               'Content-Type': 'application/json',
               'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
               'Cookie': 'JSESSIONID=B79D4AC260AEDD5C492C84B188D67761.node1; JSESSIONIDSSO=3CF16C0CA79AF2D3297E0B34F55D2C80'
            }
    conn.request("POST", f"/polarion/MyPRest/v1/rest/project/Teamcenter/setCustomField/LCS-961346", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))



#------------------------------------------------------------ solve ------------------------------------------------------------
def solve(defect_id, release_id, target_branch):
    headers = {
        'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiZjQ2ODQyYjctOTI3YTE2ZjMtM2U4ZDc0ZDEtNTk0NjY4ZmEiLCJleHAiOjE3NzA2NjE4MDAsImlhdCI6MTczOTI2NzI2MX0.BEF_nzrN7iAuKVzND_Z5xlxLRDYV1Vy3CXTgZwMPFSgfUnwA_t7BDyIOOU1DgyjfVfXv_O-QkClDdO8FUUei8Wbiy6VWArbGs5_BmwLwBMCJF457xW5hpjqvQtGsVNLAAYb0pFR8tmO-oushWr9RBiqBpEnsQdhtMrDy69EFCW5PZWeeL1USMot2-PdKBYcGW_w1lAPAL4m2IezmUHm2topn853Dq8D_OoFXLNkLJMN2ifIU_M9dQ72vFDo8I6Tx3Fg_L-uTxa6wmr_g5SaYIqmX6tFzkiezW_lV71RjfHTSc1NJAzYCIORHdb2OS8NA-NG-6e-TwWjM3KY65Np0TA',
        'Cookie': 'JSESSIONID=B79D4AC260AEDD5C492C84B188D67761.node1; JSESSIONIDSSO=3CF16C0CA79AF2D3297E0B34F55D2C80'
    }
    conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/mrRefPolarionWIs:{defect_id}", payload, headers)
    res = conn.getresponse()
    data = res.read()

    data2_json = json.loads(data.decode("utf-8"))

    if data2_json.get("error") == 500 and data2_json.get("message") == "Empty worktem list.":
        return
    else:
        codecontainer_pairs = [(item['id'], item["mrTargetBranch"]["value"]) for item in data2_json['workItems'] if item['type'] == "codecontainer" and item["mrState"]["value"] == "merged" and item["mrTargetBranch"]["value"] == target_branch]
        print(f"{defect_id}", codecontainer_pairs)

        if(len(codecontainer_pairs) > 0):
            populate_fixedIn(defect_id, release_id)

    res.close()

    
release_id = "LCS-1018392" #2406.0005
query = (
    "type:defect AND "
    f"targetRelease.KEY:{release_id} AND "
    f"approvedPatchRelease.KEY:{release_id} AND "
    f"NOT fixedInRelease.KEY:{release_id}AND "
    "NOT status:rejected AND "
    "product.KEY:(activeworkspace teamcenter)"
)

encoded_query = urllib.parse.quote(query)
url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"
conn.request("GET", url, payload, headers)
res = conn.getresponse()
data = res.read()
json_data = json.loads(data.decode("utf-8"))

target_branch = "7.1.5"
defect_ids = []
for item in json_data['data']:
    if item['type'] == "workitems":
        mystring = item['id']
        defect_id = mystring[11:]
        defect_ids.append(defect_id)
for defect_id in defect_ids:
    print(defect_id)
    solve(defect_id, release_id, target_branch)