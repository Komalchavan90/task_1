import http.client

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
  # 'Cookie': 'JSESSIONID=0BF4CB767E7E1C08226B7A50F7064422.node1; JSESSIONIDSSO=F4D32A4EE283C7FBBA390D9E34B00F9A'
}
conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/status:closed%20AND%20cpRelatedWorkitems:LCS-881215%20AND%20cpTargetNode:tc2412%20AND%20type:codecontainer", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

import http.client

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
  'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiZjQ2ODQyYjctOTI3YTE2ZjMtM2U4ZDc0ZDEtNTk0NjY4ZmEiLCJleHAiOjE3NzA2NjE4MDAsImlhdCI6MTczOTI2NzI2MX0.BEF_nzrN7iAuKVzND_Z5xlxLRDYV1Vy3CXTgZwMPFSgfUnwA_t7BDyIOOU1DgyjfVfXv_O-QkClDdO8FUUei8Wbiy6VWArbGs5_BmwLwBMCJF457xW5hpjqvQtGsVNLAAYb0pFR8tmO-oushWr9RBiqBpEnsQdhtMrDy69EFCW5PZWeeL1USMot2-PdKBYcGW_w1lAPAL4m2IezmUHm2topn853Dq8D_OoFXLNkLJMN2ifIU_M9dQ72vFDo8I6Tx3Fg_L-uTxa6wmr_g5SaYIqmX6tFzkiezW_lV71RjfHTSc1NJAzYCIORHdb2OS8NA-NG-6e-TwWjM3KY65Np0TA',
  'Cookie': 'JSESSIONID=B79D4AC260AEDD5C492C84B188D67761.node1; JSESSIONIDSSO=3CF16C0CA79AF2D3297E0B34F55D2C80'
}
conn.request("GET", "/polarion/MyPRest/v1/rest/workitems/get/type:defect AND targetRelease.KEY:LCS-1079215 AND approvedPatchRelease.KEY:LCS-1079215 AND NOT fixedInRelease.KEY:LCS-1079215 AND NOT status:rejected AND product.KEY:(activeworkspace teamcenter)", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))