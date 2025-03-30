import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template
from config import *

class SendEmail:
    @staticmethod
    def send_email(receiver_email, subject, html_content):
        # Create a MIMEMultipart message
        message = MIMEMultipart()
        message['From'] = FROM_MAIL
        message['To'] = receiver_email
        message['Subject'] = subject

        # Attach HTML content to the message
        message.attach(MIMEText(html_content, 'html'))

        # Set up the SMTP server
        with smtplib.SMTP(HOST, PORT) as server:
            server.starttls()
            server.login(FROM_MAIL, PASSWORD)
            server.sendmail(FROM_MAIL, receiver_email, message.as_string())

# Example usage
if __name__ == "__main__":
    FROM_MAIL = 'karan.shrestha05@gmail.com'
    PASSWORD = 'jafhvtebqkkxlniq'
    HOST = 'smtp.gmail.com'
    PORT = 587

    # receiver_email = 'szagham7197@student.sfbu.edu'
    receiver_email = 'kshresth328@student.sfbu.edu'
    subject = 'Subject of the email'
    html_content = """
    <html>
    <body>
        <h1>This is a HTML email</h1>
        <p>This is a paragraph in the email body.</p>
    </body>
    </html>
    """

    send_email(receiver_email, subject, html_content)
