# https://uscispolqa2/polarion/MyPRest/v1/rest/workitems/get/LCS-1114320


import http.client
import json

conn = http.client.HTTPSConnection("uscispolqa2")
payload = 'id=1'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
  'Cookie': 'JSESSIONID=5BB2F9ABE6F424BDC723C0DFC1F1E515.node1; JSESSIONIDSSO=BE2CD2870F46179F5EFC0966E196ADD3'
}
conn.request("GET", "/polarion/MyPRest/v1/rest/workitems/get/LCS-1114320", payload, headers)
res = conn.getresponse()
data = res.read()

data2=data.decode("utf-8")

data2_json=json.loads(data2)
print(data2_json['workItems'][0]['cpTargetNode']['value'])