import http.client

conn = http.client.HTTPConnection("uscispolqa2")
payload = 'id=1'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw'
}
conn.request("GET", "/polarion/MyPRest/v1/rest/workitems/get/status:closed AND cpRelatedWorkitems:LCS-881215 AND type:codecontainer AND cpTargetNode:tc2412", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))