import http.client
import json
server = "uscispolqa2"
conn = http.client.HTTPSConnection(server)

headers = {
    'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',  
    'Content-Type': 'application/json'
}


def update_fixed_in_release(work_item_id):
    payload = json.dumps({
    "fixedInRelease": "LCS-1079215"
    })
    
    conn.request("POST", f"/polarion/MyPRest/v1/rest/project/Teamcenter/setCustomField/{work_item_id}", payload, headers)
    res1 = conn.getresponse()
    data1 = res1.read()
    data11_json = json.loads(data1.decode("utf-8"))
    print(data11_json)

payload = ''
url = f"/polarion/MyPRest/v1/rest/workitems/get/type:defect%20AND%20targetRelease.KEY:LCS-1079215%20AND%20approvedPatchRelease.KEY:LCS-1079215%20AND%20NOT%20fixedInRelease.KEY:LCS-1079215%20AND%20product.KEY:(activeworkspace%20teamcenter)"
conn.request("GET", url, payload, headers)
res = conn.getresponse()
data = res.read()
data2_json = json.loads(data.decode("utf-8"))

defect_ids = []

if "workItems" in data2_json:
    for work_item in data2_json["workItems"]:
        defect_id = work_item["id"]
        defect_ids.append(defect_id)

print(defect_ids)
seperate(defect_ids)


# for defect_id in defect_ids:
#     update_fixed_in_release(defect_id)


conn.close()


