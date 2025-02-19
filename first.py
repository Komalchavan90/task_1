import http.client
import json  # Import the json module to parse JSON

# Define the connection details
conn = http.client.HTTPSConnection("uscispolqa2")
payload = 'id=1'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
    'Cookie': 'JSESSIONID=48FBCEEA11149552FD130F31D973CA19.node1; JSESSIONIDSSO=ACA8F5A094256BE52183C415264C7FAE'
}

# Make the GET request
conn.request("GET", "/polarion/MyPRest/v1/rest/workitems/get/LCS-881215/", payload, headers)


res2 = conn.getresponse()
data2 = res2.read().decode("utf-8")
data2_json = json.loads(data2)
data3=data2_json["workItems"]
print(data3[0]["targetRelease"]["value"])

type:defect AND targetRelease.KEY:$release_id AND approvedPatchRelease.KEY:$release_id AND NOT fixedInRelease.KEY:$release_id AND  product.KEY:(activeworkspace teamcenter)

