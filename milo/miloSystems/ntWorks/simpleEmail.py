#!/usr/bin/python

import smtplib

def send_smtp(sender, receivers):
    sender = ''
    receivers = ['']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test
    
    This is a test e-mail message.
    """

    try:
       # smtpObj = smtplib.SMTP('localhost') ## Use if on webserver
       smtpObj = smtplib.SMTP('mail.your-domain.com', 25)
       smtpObj.sendmail(sender, receivers, message)
       print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")