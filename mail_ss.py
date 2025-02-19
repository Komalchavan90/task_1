import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
 
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
        print("email sent")
        session.quit()
 
    @staticmethod
    def email_admin(subject, message):
        # Send email to admin
        try:
            SMTPMail.send_html_email("cismtp", 25, "", "vaishnavi.patil@siemens.com", subject, message)
        except Exception as e:
            print(f"Failed to send email: {e}")
            # Assuming TriageDefectConsumer.cleanup is a method you need to call
            # TriageDefectConsumer.cleanup(TriageDefectConsumer.path_list, TriageDefectConsumer.writer)
 
if __name__ == "__main__":
    SMTPMail.email_admin("Test Subject", "This is a test message.")