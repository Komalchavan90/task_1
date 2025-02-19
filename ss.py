import http.client

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
#   'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
#   'Cookie': 'JSESSIONID=42D79FB6B2DD3A2180872D9DE177626A.node1; JSESSIONIDSSO=47E82AFF78EC6711546EB98A1D62CCA1'
}
conn.request("GET", "/polarion/MyPRest/v1/rest/workitems/get/LCS-1111765", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))