import http.client
import json

conn = http.client.HTTPSConnection("uscispolqa2")
payload = 'id=1'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
  'Cookie': 'JSESSIONID=D902ACBDF18AA5A26CA657897F1EF700.node1; JSESSIONIDSSO=6DB0024BD23E964994F4C4AA926D7DCC'
}
conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/status:closed%20AND%20cpRelatedWorkitems:LCS-881215%20AND%20type:codecontainer%20AND%20cpTargetNode:tc2412", payload, headers)
res = conn.getresponse()
data = res.read()
data2=data.decode("utf-8")
data2_json=json.loads(data2)
# print(data2_json)

# Extracting IDs of code containers
if 'workItems' in data2_json:
    codecontainer_ids = [item['id'] for item in data2_json['workItems'] if item['type'] == "codecontainer"]
    print("Code Container IDs:", codecontainer_ids)
else:
    print("No work items found in the response.")


"/polarion/MyPRest/v1/rest/workitems/get/type:defect%20AND%20targetRelease.KEY:LCS-1079215%20AND%20approvedPatchRelease.KEY:LCS-1079215%20AND%20NOT%20fixedInRelease.KEY:LCS-1079215%20AND%20product.KEY:(activeworkspace%20teamcenter)"