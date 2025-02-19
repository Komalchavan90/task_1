import http.client
import urllib.parse
import json

######################################################## <= connection initialization part => ########################################################

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
    'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiNjg4ZTExN2YtOTI3YTE2ZjMtMDAwNjkxNDAtMDIzYjBlMWUiLCJleHAiOjE3OTk3Nzg2MDAsImlhdCI6MTczNjkyMDkyOH0.fX1y-9uK4uyd1zR1wTG2ZS7BlZoiBoeOm0UMB9_SteRCDfZ2YO9AfQEAr4aQ3q00bHs5TZFvJLXBNy3fdrUIA2W8rVuDUg79dgy3i7phczN5hV4KwFjhqm5VIXQ4QuPeoQk3IHG1JCZqNsl_XYM03Q7gJ-7OZV4wENpisiALiim4l9wxDit3CWIBskNKr2UGn1OHlDsi6sjj7_B8QGMH821vSiN61CvaetNxaumM4MvcLeYCQQQ_dACh15XUgaXPHTKEW_UpN68BfPWA6NkqAXEagCPE2eSMJ5boWwZOeg5yI91qRY13ugjar1fcl4RDAmot3Vc-yF354G5jnJmDuQ',
    'Cookie': 'JSESSIONID=81913C43E42C82D8842E4B6A792728F2.node1; JSESSIONIDSSO=D866BE0E699666A2FD46695C6EDFFB8D'
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

######################################################## <= Helper 2 function  => ########################################################

def helper_two(defect_id, cp_target_node):
    payload = json.dumps({
        "fixedInRelease": "LCS-1079215"
    })
    defect_id="LCS-943973"

    conn.request("POST", f"/polarion/MyPRest/v1/rest/project/Teamcenter/setCustomField/{defect_id}", payload, headers)
    res3 = conn.getresponse()
    data3 = res3.read()
    data33_json = json.loads(data3.decode("utf-8"))
    print(data33_json)

######################################################## <= Helper 1 function  => ########################################################

def helper_one(defect_id, cp_target_node):
    conn.request(
        "GET",
        f"/polarion/MyPRest/v1/rest/workitems/get/status:closed%20AND%20cpRelatedWorkitems:{defect_id}%20AND%20type:codecontainer%20AND%20cpTargetNode:{cp_target_node}",
        payload,
        headers,
    )
    res2 = conn.getresponse()

    if res2 is None:
        print("The response is null")
    else:
        data2 = res2.read()
        data22 = data2.decode("utf-8")
        data22_json = json.loads(data22)
        # print(data22_json)

        if 'workItems' in data22_json:
            codecontainer_ids = [item['id'] for item in data22_json['workItems'] if item['type'] == "codecontainer"]
            print("Code Container IDs:", codecontainer_ids)
            if len(codecontainer_ids) > 0:
                for codecontainer_id in codecontainer_ids:
                    conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/{codecontainer_id}", payload, headers)
                    res3 = conn.getresponse()
                    data3 = res3.read()

                    data33 = data3.decode("utf-8")
                    count = 0
                    data33_json = json.loads(data33)
                    print(data33_json['workItems'][0]['cpTargetNode']['value'])

                    if data33_json['workItems'][0]['cpTargetNode']['value'] == cp_target_node:
                        count += 1
                    if count >= 1:
                        helper_two(defect_id, cp_target_node)
                        
        else:
            print("No work items found in the response.")

    res2.close()

######################################################## <= fetching auto deferred defects => ########################################################

encoded_query = urllib.parse.quote(query)

cp_target_node = "tc2412"

url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"
conn.request("GET", url, payload, headers)
res = conn.getresponse()
data = res.read()

json_data = json.loads(data.decode("utf-8"))
for item in json_data['data']:
    if item['type'] == "workitems":
        mystring = item['id']
        defect_id = mystring[11:]
        helper_one(defect_id, cp_target_node)