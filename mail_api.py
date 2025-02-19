import http.client
import json
import re

def helper(s1,s2):
    regex = rf"\b{s1}\b.*\b{s2}\b|\b{s2}\b.*\b{s1}\b"
    
    if "data" in data and isinstance(data["data"], list):
        for art in data["data"]:
            if "teamsInTrain" in art and isinstance(art["teamsInTrain"], list):
                for team in art["teamsInTrain"]:
                    if "teamMembers" in team and isinstance(team["teamMembers"], list):
                        for member in team["teamMembers"]:
                            if "userEmail" in member: 
                                email = member["userEmail"]
                            if re.search(regex, email, re.IGNORECASE):
                                matches.append(email)


conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
defect_id="LCS-133897"
headers = {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
  'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
}
conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/{defect_id}", payload, headers)
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))

data2 = data.decode("utf-8")
data2_json = json.loads(data2)

# team_backlog_name = data2_json['workItems'][0]['teamBacklog']['value']['name']
if "workItems" in data2_json :
    for i in range(0, len(data2_json['workItems'])):
        if "teamBacklog" in data2_json['workItems'][i]:
            team_backlog_name=data2_json['workItems'][i]['teamBacklog']['value']['name']
        else:
            continue
    print("found")

print(f"Team Backlog Name: {team_backlog_name}")

with open('team-backlog.json', 'r') as f:
    team_backlog = json.load(f)

# print(team_backlog)
validators_list=[]

for i in range (0, len(team_backlog.get(team_backlog_name, [None]))):
    validators_list.append(team_backlog.get(team_backlog_name, [None])[i])

print(f"Validators List: {validators_list}")



with open('users.json', 'r') as f:
    data = json.load(f)

for i in range(0, len(validators_list)):
    s1, s2 = validators_list[i].split()  # Splitting into two parts
    s1=s1.replace(",", "")
    s2=s2.replace(" (EXT)", "")

    s1=s1.replace(" (EXT)", "")
    s2=s2.replace(",", "")
    matches=[]
    helper(s1,s2)
    


for match in matches:
    print(match)


