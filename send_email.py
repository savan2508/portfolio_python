import re
import smtplib
import os
import ssl
import dns.resolver
from dotenv import load_dotenv


load_dotenv()

gmail_username = os.getenv('GMAIL_USERNAME')
gmail_password = os.getenv('GMAIL_PASSWORD')

host = "smtp.gmail.com"
port = 465

context = ssl.create_default_context()


def send_email(user_name, user_email, user_message):
    message = f"""Subject: New Message from {user_name}\n\n
    Name: {user_name}
    Email: {user_email}\n\n
    {user_message}"""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(gmail_username, gmail_password)
        server.sendmail(
            from_addr=gmail_username,
            to_addrs=gmail_username,
            msg=message
        )


def valid_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False

    _, domain = email.split("@")

    try:
        dns.resolver.resolve(domain, "MX")
        return True
    except dns.resolver.NXDOMAIN:
        return False
    except dns.resolver.NoAnswer:
        return False
    except dns.resolver.Timeout:
        return False
