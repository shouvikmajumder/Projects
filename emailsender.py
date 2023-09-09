import smtplib
import ssl 
from email.message import EmailMessage

# Get user input for subject and password
subject = input("What do you want the subject to be?: ") 
password = input("Enter password: ")

# Set up the message object
message = EmailMessage()
message["Subject"] = subject
message["From"] = "shouvikprism@gmail.com"
message["To"] = "shouvikprism@gmail.com"
message.set_content("This is a test email from python")

# Connect to the SMTP server and send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login("shouvikprism@gmail.com", password)
    server.send_message(message)

print("Email sent successfully!")
