import smtplib
import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from emailcreator import *
from processing import clean_data



def send_mail(service_provider,app_password,sender_email,receiver_email,subject,message):
    SMTP_SERVER = f"smtp.{service_provider}.com"
    SMTP_PORT = 587
    USERNAME = sender_email
    PASSWORD = app_password  
    sender_email =sender_email
    receiver_email =receiver_email
    subject = subject
    body =message
    # Create MIME message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            print(server.login(USERNAME, PASSWORD) )
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

