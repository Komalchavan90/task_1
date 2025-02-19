import http.client
import urllib.parse
import json

######################################################## <= connection initialization part => ########################################################

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
    'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiZjQ2ODQyYjctOTI3YTE2ZjMtM2U4ZDc0ZDEtNTk0NjY4ZmEiLCJleHAiOjE3NzA2NjE4MDAsImlhdCI6MTczOTI2NzI2MX0.BEF_nzrN7iAuKVzND_Z5xlxLRDYV1Vy3CXTgZwMPFSgfUnwA_t7BDyIOOU1DgyjfVfXv_O-QkClDdO8FUUei8Wbiy6VWArbGs5_BmwLwBMCJF457xW5hpjqvQtGsVNLAAYb0pFR8tmO-oushWr9RBiqBpEnsQdhtMrDy69EFCW5PZWeeL1USMot2-PdKBYcGW_w1lAPAL4m2IezmUHm2topn853Dq8D_OoFXLNkLJMN2ifIU_M9dQ72vFDo8I6Tx3Fg_L-uTxa6wmr_g5SaYIqmX6tFzkiezW_lV71RjfHTSc1NJAzYCIORHdb2OS8NA-NG-6e-TwWjM3KY65Np0TA',
    'Content-Type': 'application/json'
}
headers2 = {
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
  'Cookie': 'JSESSIONID=FAC71D9D92DE16CC42E2526F58C4DE3F.node1; JSESSIONIDSSO=4DC82F35F6BEE279BF9CEC19057EBEDD'
}
query = (
    "type:defect AND "
    "targetRelease.KEY:LCS-1079215 AND "
    "approvedPatchRelease.KEY:LCS-1079215 AND "
    "NOT fixedInRelease.KEY:LCS-1079215 AND "
    "NOT status:rejected AND "
    "product.KEY:(activeworkspace teamcenter) AND "
    "NOT validatedIn.KEY:LCS-1079215"
)

######################################################## <= Helper 4 function => ########################################################
# def helper_four(defect_id, cp_target_node):
    

######################################################## <= Helper 2 function => ########################################################

# def helper_two(defect_id, cp_target_node):
#     payload = json.dumps({
#         "fixedInRelease": "LCS-1079215"
#     })

#     defect_id="LCS-943078"
    
#     conn.request("POST", f"/polarion/MyPRest/v1/rest/project/Teamcenter/setCustomField/{defect_id}", payload, headers)
#     res1 = conn.getresponse()
#     if res1.status != 200:
#         print(f"Failed to update defect {defect_id}. Status: {res1.status}")
#         return
#     data1 = res1.read()
#     try:
#         data11_json = json.loads(data1.decode("utf-8"))
#         print(data11_json)
#     except json.JSONDecodeError:
#         print(f"Failed to decode JSON response for defect {defect_id}: {data1}")
#     res1.close()

######################################################### <= Helper 3 function => #######################################################

# def helper_three(defect_id, cp_target_node, codecontainer_ids):
#     for codecontainer_id in codecontainer_ids:
#         conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/{codecontainer_id}", payload, headers)
#         res3 = conn.getresponse()
#         data3 = res3.read()

#         data33 = data3.decode("utf-8")
#         count = 0
#         try:
#             data33_json = json.loads(data33)
#         except json.JSONDecodeError:
#             print(f"Failed to decode JSON response for code container {codecontainer_id}: {data33}")
#             continue

#         print(data33_json['workItems'][0]['cpTargetNode']['value'])

#         if data33_json['workItems'][0]['cpTargetNode']['value'] == cp_target_node:
#             count += 1
#         if count >= 1:
#             print("later")
#             helper_two(defect_id, cp_target_node)
#             helper_four(defect_id, cp_target_node)


# ######################################################## <= Helper 1 function => ########################################################

# def helper_one(defect_id, cp_target_node):
#     conn.request(
#         "GET",
#         f"/polarion/MyPRest/v1/rest/workitems/get/status:closed%20AND%20cpRelatedWorkitems:{defect_id}%20AND%20type:codecontainer%20AND%20cpTargetNode:{cp_target_node}",
#         payload,
#         headers,
#     )
#     res2 = conn.getresponse()
#     data2 = res2.read()
#     data22 = data2.decode("utf-8")
#     data22_json = json.loads(data22)

#     if 'workItems' in data22_json:
#         codecontainer_ids = [item['id'] for item in data22_json['workItems'] if item['type'] == "codecontainer"]
#         print(f"Defect id: {defect_id} Code Container IDs:", codecontainer_ids)
#         if len(codecontainer_ids) > 0:
#             helper_three(defect_id, cp_target_node, codecontainer_ids)
#     else:
#         print("No work items found in the response.")

#     res2.close()

######################################################## <= fetching auto deferred defects => ########################################################

######################################################## <= separating defects based on status => ########################################################
def get_defect_details(defect_id):
    """Fetch defect details from API and handle errors."""
   
    conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/validatedIn.KEY:LCS-1079215%20AND%20id:{defect_id}", payload, headers)
    res = conn.getresponse()
        
    data = res.read()
    if res is None:
        print("The response is null")
    else:
        print(json.loads(data.decode("utf-8")))
        # Check for valid response
        print("-----------------------------------------------")

def seperate_ids(defect_ids, release_id):
    validated = []
    not_validated = []

    for defect_id in defect_ids:
        defect_data = get_defect_details(defect_id)
        # if not defect_data or "workItems" not in defect_data:
        #     not_validated.append(defect_id)
        #     continue

        # is_validated = any(
        #     "validatedIn" in item and any(v['id'] == release_id for v in item['validatedIn'].get('value', []))
        #     for item in defect_data['workItems']
        # )

        # if is_validated:
        #     validated.append(defect_id)
        # else:
        #     not_validated.append(defect_id)

    
    for defect_id in validated:
        print(f"Defect {defect_id} is validated")
    for defect_id in not_validated:
        print(f"Defect {defect_id} is not validated")

    # return defect_ids_validated, defect_ids_not_validated

encoded_query = urllib.parse.quote(query)

cp_target_node = "tc2412"

url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"
conn.request("GET", url, payload, headers)
res = conn.getresponse()
data = res.read()

json_data = json.loads(data.decode("utf-8"))
# print(json_data)
defect_ids = []
for item in json_data['data']:
    if item['type'] == "workitems":
        mystring = item['id']
        defect_id = mystring[11:]
        defect_ids.append(defect_id)
        # helper_one(defect_id, cp_target_node)
seperate_ids(defect_ids, "LCS-1079215")