import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendActual_email(match, defect_id, cp_target_node):
    smtp_server = 'smtp.siemens.com'
    smtp_port = 587
    smtp_user = 'komal.chavan@siemens.com'
    smtp_password = 'SatyajitGaikwad!90'
    from_email = 'komal.chavan@siemens.com'
    to_email = match[0]
    print(to_email)
    subject = 'Test Email'
    body = f'Please validate this defect {defect_id}'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
        print('Email sent successfully')
    except smtplib.SMTPException as e:
        print(f'Failed to send email: {e}')
    finally:
        try:
            server.quit()
        except smtplib.SMTPServerDisconnected:
            print('Server disconnected before quit could be called')

# Example usage
matches = ['dishitaa.mahale@siemens.com']
defect_id = 'LCS-133897'
cp_target_node = 'tc2412'
sendActual_email(matches, defect_id, cp_target_node)