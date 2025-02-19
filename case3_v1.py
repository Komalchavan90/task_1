import http.client

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
  'Cookie': 'JSESSIONID=D6DE37D9FB23815A1C77EFDBBEDC3E74.node1; JSESSIONIDSSO=3C0475401729CD013CB9DC4245449E5A'
}
conn.request("GET", "/polarion/MyPRest/v1/rest/workitems/get/type:defect AND targetRelease.KEY:LCS-1079215 AND approvedPatchRelease.KEY:LCS-1079215 AND NOT fixedInRelease.KEY:LCS-1079215 AND NOT status:rejected AND product.KEY:(activeworkspace teamcenter)", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))