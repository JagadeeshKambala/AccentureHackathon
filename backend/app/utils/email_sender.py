import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email: str, subject: str, body: str, from_email="hr@example.com"):
    """
    Send a plain text email via local SMTP server.
    """
    try:
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("localhost", 25) as server:
            server.send_message(msg)
            print(f"Email sent to {to_email}")

        return True

    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
