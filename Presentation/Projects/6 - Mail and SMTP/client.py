import smtplib

smtp_server = "localhost"
port = 1025

sender = "ramtinkosari@gmail.com"
recipient = "localhost@local.com"
message = """\
From: ramtinkosari@gmail.com
To: localhost@local.com
Subject: Test Email

10 + 14 = 25 ?"""

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.sendmail(sender, recipient, message)
    print("Email Sent Successfully!")
except Exception as e:
    print(f"Error: {e}")
