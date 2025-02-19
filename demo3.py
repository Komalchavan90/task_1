import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
smtp_port = 485 # Port for SSL
smtp_user = 'kc8781686@gmail.com'  # Replace with your email address
smtp_password = 'gvfy ysfz jdyo nohv'  # Replace with your email password

# Email details
from_email = 'kc8781686@gmail.com'
to_email = 'komalchavans176@gmail.com'  # Replace with the recipient's email address
subject = 'Test Email'
body = 'Hello, This is an email from Polarion.'

# Create the email message
message = MIMEMultipart()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    # Connect to the SMTP server
    server = smtplib.SMTP_SSL(smtp_server, smtp_port,timeout=120)
    server.login(smtp_user, smtp_password)
    
    # Send the email
    server.sendmail(from_email, to_email, message.as_string())
    print('Email sent successfully')
except smtplib.SMTPException as e:
    print(f'Failed to send email: {e}')
except TimeoutError as e:
    print(f'Connection timed out: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    try:
        # server.quit()
        print("anything")
    except smtplib.SMTPServerDisconnected:
        print('Server disconnected before quit could be called')
    except Exception as e:
        print(f'An error occurred while closing the connection: {e}')