import smtplib, ssl

host = "smtp.gmail.com"
port = 465

user_name = "iwillthrowaway001@gmail.com"
password = "jejd wksm hojs svos"

receiver = "iwillthrowaway001@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hello World
Hi!
How are You?
Bye!

"""
with smtplib.SMTP_SSL(host, port, context=context) as server:

    server.login(user_name, password)
    server.sendmail(user_name, receiver, message)