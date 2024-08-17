import smtplib
import json

def send_email(subject, body, sender, recipients, password):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        
        message = f"Subject: {subject}\n\n{body}"
        smtp.sendmail(sender, recipients, message)
    
    print('Mail sent successfully')

def load_emails_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data.get('recipients', [])

# Usage
subject = 'Sending email with Python'
body = 'Testing my Python program'
sender = 'email@email.com'
password = 'password'

# Load recipients from JSON file
recipients = load_emails_from_json('emails.json')
print(recipients)

send_email(subject, body, sender, recipients, password)
