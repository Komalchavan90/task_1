import http.client

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
  'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiNjg4ZTExN2YtOTI3YTE2ZjMtMDAwNjkxNDAtMDIzYjBlMWUiLCJleHAiOjE3OTk3Nzg2MDAsImlhdCI6MTczNjkyMDkyOH0.fX1y-9uK4uyd1zR1wTG2ZS7BlZoiBoeOm0UMB9_SteRCDfZ2YO9AfQEAr4aQ3q00bHs5TZFvJLXBNy3fdrUIA2W8rVuDUg79dgy3i7phczN5hV4KwFjhqm5VIXQ4QuPeoQk3IHG1JCZqNsl_XYM03Q7gJ-7OZV4wENpisiALiim4l9wxDit3CWIBskNKr2UGn1OHlDsi6sjj7_B8QGMH821vSiN61CvaetNxaumM4MvcLeYCQQQ_dACh15XUgaXPHTKEW_UpN68BfPWA6NkqAXEagCPE2eSMJ5boWwZOeg5yI91qRY13ugjar1fcl4RDAmot3Vc-yF354G5jnJmDuQ',
  'Cookie': 'JSESSIONID=790354E5ED41DB45BAA85BE5A4DCE02A.node1; JSESSIONIDSSO=6DB0024BD23E964994F4C4AA926D7DCC'
}
conn.request("GET", "/polarion/rest/v1/projects/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))