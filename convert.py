import json
import re

s1 = "Shubham"
s2 = "bhandari (EXT)"

s2 = s2.replace(",", "")
s1= s1.replace(" (EXT)", "")

s1 = s1.replace(",", "")
s2= s2.replace(" (EXT)", "")
# print(s2)

with open('users.json', 'r') as f:
    data = json.load(f)

regex = rf"\b{s1}\b.*\b{s2}\b|\b{s2}\b.*\b{s1}\b"

matches = []

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

for match in matches:
    print(match)



# fixed in no 
# validated in  yes

# in this above case code will handle

# fixed in no
# validated in no 
# notify