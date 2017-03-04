import smtplib, os

try:
    email_address = os.environ['EMAIL_ADDRESS']
    email_passwd = os.environ['EMAIL_PASSWD']
except:
    print 'Env variables not set please set EMAIL_ADDRESS and EMAIL_PASSWD.'

def notify(notification_method, receiver_address, message):
    if notification_method == 'email':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, email_passwd)
        server.sendmail(email_address, receiver_address, message)
        server.quit()
    else:
        print 'Local Notification: ' + message
