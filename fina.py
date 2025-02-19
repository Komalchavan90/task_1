import http.client
import urllib.parse
import json
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

######################################################## <= connection initialization part => ########################################################

conn = http.client.HTTPSConnection("uscispolqa2")
payload = ''
headers = {
    'Authorization': 'Bearer eyJraWQiOiI5Mjg4ZmExNC05MjdhMTZmMy0xODI3YmY4NC1iZmIyMzNlNSIsInR5cCI6IkpXVCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJ6MDA1MmpwbSIsImlkIjoiZjQ2ODQyYjctOTI3YTE2ZjMtM2U4ZDc0ZDEtNTk0NjY4ZmEiLCJleHAiOjE3NzA2NjE4MDAsImlhdCI6MTczOTI2NzI2MX0.BEF_nzrN7iAuKVzND_Z5xlxLRDYV1Vy3CXTgZwMPFSgfUnwA_t7BDyIOOU1DgyjfVfXv_O-QkClDdO8FUUei8Wbiy6VWArbGs5_BmwLwBMCJF457xW5hpjqvQtGsVNLAAYb0pFR8tmO-oushWr9RBiqBpEnsQdhtMrDy69EFCW5PZWeeL1USMot2-PdKBYcGW_w1lAPAL4m2IezmUHm2topn853Dq8D_OoFXLNkLJMN2ifIU_M9dQ72vFDo8I6Tx3Fg_L-uTxa6wmr_g5SaYIqmX6tFzkiezW_lV71RjfHTSc1NJAzYCIORHdb2OS8NA-NG-6e-TwWjM3KY65Np0TA',
    'Content-Type': 'application/json'
}
headers2 = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
    'Cookie': 'JSESSIONID=5D856C9B3A68EDB6A70E0520CF005041.node1; JSESSIONIDSSO=DE5E8CA0CF7B5E631586E34DF0569353'
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



#----------------------------------------send email -----------------------------------------------

class SMTPMail:
    def __init__(self):
        pass

    @staticmethod
    def send_html_email(host, port, from_address, to_address, subject, message):
        # Set SMTP server properties
        properties = {
            "mail.smtp.host": host,
            "mail.smtp.port": port,
            "mail.smtp.auth": "false"
        }

        # Create a new session
        session = smtplib.SMTP(host, port)

        # Create a new e-mail message
        msg = MIMEMultipart()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject
        msg['Date'] = datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")

        # Set plain text message
        msg.attach(MIMEText(message, 'html'))

        # Send the e-mail
        session.sendmail(from_address, to_address, msg.as_string())
        session.quit()

    @staticmethod
    def email_admin(subject, message):
        # Send email to admin
        try:
            SMTPMail.send_html_email("cismtp", 25, "komal.chavan@siemens.com", "dishitaa.mahale@siemens.com", subject, message)
        except Exception as e:
            print(f"Failed to send email: {e}")

def send_mail(matches, defect_id):
    subject = f"Defect Notification for {defect_id}"
    message = f"The following users are associated with defect {defect_id}:<br>" + "<br>".join(matches)
    SMTPMail.email_admin(subject, message)

#-----------------------------------------helper-mail function --------------------------------------

def helper(s1, s2, matches, defect_id):
    with open('users.json', 'r') as f:
        data = json.load(f)
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

    for match in matches:
        print(match)
    
    send_mail(matches, defect_id)

#-----------------------------------------helper-mail function --------------------------------------
def helper_mail(defect_id, cp_target_node):
    defect_id = "LCS-943073"
    headers = {
            'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw'
    }
    conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/{defect_id}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    data2 = data.decode("utf-8")
    data2_json = json.loads(data2)

    if "workItems" in data2_json:
        for i in range(0, len(data2_json['workItems'])):
            if "teamBacklog" in data2_json['workItems'][i]:
                team_backlog_name = data2_json['workItems'][i]['teamBacklog']['value']['name']
            else:
                continue
        print("found")

    print(f"Team Backlog Name: {team_backlog_name}")

    with open('team-backlog.json', 'r') as f:
        team_backlog = json.load(f)

    validators_list = []

    for i in range(0, len(team_backlog.get(team_backlog_name, [None]))):
        validators_list.append(team_backlog.get(team_backlog_name, [None])[i])

    print(f"Validators List: {validators_list}")

    
    
    # if(len(validators_list) > 0):
    #     print("no data found for team backlog")
    #     for i in range(0, len(validators_list)):
    #         s1, s2 = validators_list[i].split()  # Splitting into two parts
    #         s1 = s1.replace(",", "")
    #         s2 = s2.replace(" (EXT)", "")

    #         s1 = s1.replace(" (EXT)", "")
    #         s2 = s2.replace(",", "")
    #         matches = []
    #         helper(s1, s2, matches, defect_id)
    s1="Padar"
    s2="Mangesh"
    helper(s1, s2, [], defect_id)

#-----------------------------------------helper one function --------------------------------------

def helper_one(defect_id, cp_target_node):
    headers = {
            'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw'
    }
    print(defect_id)
    conn.request("GET", f"/polarion/MyPRest/v1/rest/workitems/get/status:closed%20AND%20cpRelatedWorkitems:LCS-881215%20AND%20cpTargetNode:tc2412%20AND%20type:codecontainer", payload, headers)
    res = conn.getresponse()
    

    print(res.status)
    if res is None:
        print("The response is null")
    else:
        data2 = res.read()
        data22_json=json.loads(data2)
        if "workItems" in data22_json:
            codecontainer_ids = [item['id'] for item in data22_json['workItems'] if item['type'] == "codecontainer"]
            # print("Code Container IDs:", codecontainer_ids)
            if len(codecontainer_ids) > 0:
                print("send email")
                helper_mail(defect_id, cp_target_node)
                helper_two(defect_id, cp_target_node)
                # return
        
    res.close()
#----------------------------------------------- solve validated ---------------------------------------

def helper_two(defect_id, cp_target_node):
    defect_id = "LCS-943073"
    payload = json.dumps({
        "fixedInRelease": "LCS-1021360"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ejAwNTJqcG06U2F0eWFqaXRHYWlrd2FkITkw',
        'Cookie': 'JSESSIONID=5D856C9B3A68EDB6A70E0520CF005041.node1; JSESSIONIDSSO=DE5E8CA0CF7B5E631586E34DF0569353'
    }
    conn.request("POST", f"/polarion/MyPRest/v1/rest/project/Teamcenter/setCustomField/{defect_id}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def solve_validated(validated, release_id):
    print("solve defects called")
    validated.append("LCS-943076")
    cp_target_node = "tc2412"
    for defect_id in validated:
        helper_two(defect_id, cp_target_node)

#----------------------------------------------- solve not validated ---------------------------------------

def solve_notValidated(not_validated, release_id):
    print(len(not_validated))
    for defect_id in not_validated:
        helper_one(defect_id, "tc2412")

#----------------------------------------------- pass for solving individually ------------------------

def solve_defects(validated, not_validated, release_id):
    #solve_validated(validated, release_id)
    solve_notValidated(not_validated, release_id)

#-----------------------------------------------get response --------------------------------------

def check_defect_validation(defect_id, release_id):
    validated = []
    not_validated = []
    """Checks if a defect is validated based on API response."""
    query2 = (
        "type:defect AND"
        f"NOT validatedIn.KEY:{release_id} AND"
        f"id:{defect_id}"
    )

    encoded_query2 = urllib.parse.quote(query2)
    url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query2}"
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    if not data:
        print("Empty response")
        return False
    json_data = json.loads(data.decode("utf-8"))

    if json_data.get("error") == 500 and json_data.get("message") == "Empty worktem list.":
        return True
    else:
        return False

    res.close()

# ------------------------------------------------------classify defects-----------------------------------------

def classify_defects(defect_ids, release_id):
    """Classifies defects as validated or not validated."""
    validated = []
    not_validated = []

    for defect_id in defect_ids:
        # print(defect_id)
        if check_defect_validation(defect_id, release_id):
            validated.append(defect_id)
        else:
            not_validated.append(defect_id)
    print(len(validated))

    print(len(not_validated))
    solve_defects(validated, not_validated, release_id)

# ------------------------------------------------------get the auto deferral defects------------------------------------------

encoded_query = urllib.parse.quote(query)

cp_target_node = "tc2412"

url = f"/polarion/rest/v1/projects/Teamcenter/workitems?query={encoded_query}"
conn.request("GET", url, payload, headers)
res = conn.getresponse()
data = res.read()

release_id = "LCS-1079215"

json_data = json.loads(data.decode("utf-8"))
# print(json_data)
defect_ids = []
for item in json_data['data']:
    if item['type'] == "workitems":
        mystring = item['id']
        defect_id = mystring[11:]
        defect_ids.append(defect_id)
        # helper_one(defect_id, cp_target_node)
classify_defects(defect_ids, release_id)
res.close()