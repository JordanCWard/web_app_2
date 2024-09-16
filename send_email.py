import smtplib, ssl

host = "smtp.gmail.com"
port = 465

# Python Mega Course lecture 221 to set this up
username = "jordancward@gmail.com"
password = "bzbaqtukldocffkd"

receiver = "moveshhh8@gmail.com"

# to add a subject, must put Subject:
message = """Subject: First message
This is a message in the email?
"""

with smtplib.SMTP_SSL(host, port) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)