import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, smtp_port, smtp_username, smtp_password, to_email, subject, body):
    from_email = f"Automation <{smtp_username}>"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Get input environment variables passed by the GitHub Action
    smtp_server = os.getenv('INPUT_SMTP_SERVER')
    smtp_port = os.getenv('INPUT_SMTP_PORT')
    smtp_username = os.getenv('INPUT_SMTP_USERNAME')
    smtp_password = os.getenv('INPUT_SMTP_PASSWORD')
    to_email = os.getenv('INPUT_TO_EMAIL')
    subject = os.getenv('INPUT_SUBJECT')
    body = os.getenv('INPUT_BODY')

    # Call the function to send the email
    send_email(smtp_server, smtp_port, smtp_username, smtp_password, to_email, subject, body)
