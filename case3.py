import http.client
import json
import urllib.parse


server = "uscispolqa2"
conn = http.client.HTTPSConnection(server)

version_map={
    #active workspace version: teamcenter version
    #6.3
    "6.3.13":"Teamcenter 14.3.0.13",
    "6.3.12":"Teamcenter 14.3.0.12",
    "6.3.11":"Teamcenter 14.3.0.11",
    "6.3.10":"Teamcenter 14.3.0.10",
    "6.3.9":"Teamcenter 14.3.0.9",
    "6.3.8":"Teamcenter 14.3.0.8",
    "6.3.7":"Teamcenter 14.3.0.7",

    #6.2
    "6.2.14":"Teamcenter 2406.0001.0101",
    "6.2.13":"Teamcenter 14.2.0.13",
    "6.2.12":"Teamcenter 14.2.0.12",
    "6.2.11":"Teamcenter 14.2.0.11",
    "6.2.10":"Teamcenter 14.2.0.10",
    "6.2.9":"Teamcenter 14.2.0.9",
   
    #6.1
    "6.1.14":"Teamcenter Visualization 14.1.0.14",
    "6.1.13":"Teamcenter 14.1.0.13"
    
}


version_map_id={
    #active workspace workitem id: teamcenter id
    #6.3
    "LCS-1082620":"LCS-1079272",
    "LCS-1082560":"LCS-1079215",
    "LCS-1017358":"LCS-1017305",
    "LCS-1016749":"LCS-1016696",
    "LCS-999637":"LCS-999691",
    "LCS-968625":"LCS-965625",
    "LCS-950708":"LCS-950659",

    #6.2
    "LCS-1024065":"LCS-1024030",
    "LCS-1023948":"LCS-1023908",
    "LCS-1021405":"LCS-1021360",
    "LCS-996577":"LCS-996617",
    "LCS-948834":"LCS-924836",

    #6.1
    "LCS-996538":"LCS-994676",
    "LCS-953612":"LCS-953479"

}
conn = http.client.HTTPSConnection("uscispolqa2")

def solve3(defect_ids):
    for defect_id in defect_ids:
        print(defect_id)

        cp_target_node = 0


def solve2(defect_id):

    payload = ''
    headers = {
    'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiZjQ2ODQyYjctOTI3YTE2ZjMtM2U4ZDc0ZDEtNTk0NjY4ZmEiLCJleHAiOjE3NzA2NjE4MDAsImlhdCI6MTczOTI2NzI2MX0.BEF_nzrN7iAuKVzND_Z5xlxLRDYV1Vy3CXTgZwMPFSgfUnwA_t7BDyIOOU1DgyjfVfXv_O-QkClDdO8FUUei8Wbiy6VWArbGs5_BmwLwBMCJF457xW5hpjqvQtGsVNLAAYb0pFR8tmO-oushWr9RBiqBpEnsQdhtMrDy69EFCW5PZWeeL1USMot2-PdKBYcGW_w1lAPAL4m2IezmUHm2topn853Dq8D_OoFXLNkLJMN2ifIU_M9dQ72vFDo8I6Tx3Fg_L-uTxa6wmr_g5SaYIqmX6tFzkiezW_lV71RjfHTSc1NJAzYCIORHdb2OS8NA-NG-6e-TwWjM3KY65Np0TA',
    'Content-Type': 'application/json'
    }
    query = (
    "type:defect AND "
    f"targetRelease.KEY:{defect_id} AND "
    f"approvedPatchRelease.KEY:{defect_id} AND "
    f"NOT fixedInRelease.KEY:{defect_id} AND "
    "NOT status:rejected AND "
    "product.KEY:(activeworkspace teamcenter) "
    )

    encoded_query = urllib.parse.quote(query)
    
    url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"
    payload = ''
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    data2_json = json.loads(data.decode("utf-8"))
    # print(data2_json)
    defect_ids = []
    if "data" in data2_json:
        for work_item in data2_json["data"]:
            defect_id = work_item["id"]
            mystring = defect_id
            defect_id = mystring[11:]
            defect_ids.append(defect_id)
    
    solve3(defect_ids)


def solve(key, value):
    defect_id1="LCS-1082560"
    defect_id2="LCS-1079215"
    solve2(defect_id1)

solve(1,2)
# for key, value in version_map_id.items():
#     # solve(key, value)
#     # print(key, value)