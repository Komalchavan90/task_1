import http.client
import json
import urllib.parse

conn = http.client.HTTPSConnection("uscispolqa2")
payload = 'id=1'

headers2 = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
  'Cookie': 'JSESSIONID=D902ACBDF18AA5A26CA657897F1EF700.node1; JSESSIONIDSSO=6DB0024BD23E964994F4C4AA926D7DCC'
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiNjg4ZTExN2YtOTI3YTE2ZjMtMDAwNjkxNDAtMDIzYjBlMWUiLCJleHAiOjE3OTk3Nzg2MDAsImlhdCI6MTczNjkyMDkyOH0.fX1y-9uK4uyd1zR1wTG2ZS7BlZoiBoeOm0UMB9_SteRCDfZ2YO9AfQEAr4aQ3q00bHs5TZFvJLXBNy3fdrUIA2W8rVuDUg79dgy3i7phczN5hV4KwFjhqm5VIXQ4QuPeoQk3IHG1JCZqNsl_XYM03Q7gJ-7OZV4wENpisiALiim4l9wxDit3CWIBskNKr2UGn1OHlDsi6sjj7_B8QGMH821vSiN61CvaetNxaumM4MvcLeYCQQQ_dACh15XUgaXPHTKEW_UpN68BfPWA6NkqAXEagCPE2eSMJ5boWwZOeg5yI91qRY13ugjar1fcl4RDAmot3Vc-yF354G5jnJmDuQ',
    'Cookie': 'JSESSIONID=790354E5ED41DB45BAA85BE5A4DCE02A.node1; JSESSIONIDSSO=6DB0024BD23E964994F4C4AA926D7DCC'
}

query = (
    "type:defect AND "
    "targetRelease.KEY:LCS-1079215 AND "
    "approvedPatchRelease.KEY:LCS-1079215 AND "
    "NOT fixedInRelease.KEY:LCS-1079215 AND "
    "product.KEY:(activeworkspace teamcenter)"
)


    
        # data22_json = json.loads(data22)
        # if 'workItems' in data22_json:
        #     codecontainer_ids = [item['id'] for item in data22_json['workItems'] if item['type'] == "codecontainer"]
        #     print("Code Container IDs:", codecontainer_ids) ## list size if > 0 -> mail 
            
    
   


encoded_query = urllib.parse.quote(query)

url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"
conn.request("GET", url, payload, headers)

res = conn.getresponse()
data = res.read()
data2=data.decode("utf-8")
data2_json=json.loads(data2)

cp_target_node="tc2412"
for item in data2_json['data']:
    if item['type'] == "workitems":
        mystring=item['id']
        mystring2=mystring[11:]
        solve(mystring2,cp_target_node)


defect_ids = [item['id'] for item in data2_json['data'] if item['type'] == "workitems"]


