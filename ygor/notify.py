import smtplib, os, sys

try:
    email_address = os.environ['IGOR_EMAIL_ADDRESS']
    email_passwd = os.environ['IGOR_EMAIL_PASSWD']
    receiver_address = os.environ['IGOR_RECEIVER_ADDRESS']
except:
    print 'Env variables not set please set IGOR_EMAIL_ADDRESS, IGOR_EMAIL_PASSWD and IGOR_RECEIVER_ADDRESS.'
    sys.exit(1)

def notify(notification_method, receiver_address, url):
    html_mail = '''\
    Alert! change on CHANGETHIS.

    Hi there was a change on one of your monitored sites, please follow the link bellow:

    CHANGETHIS
    '''
    html_mail = html_mail.replace('CHANGETHIS', url)
    if notification_method == 'email':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_address, email_passwd)
        server.sendmail(email_address, receiver_address, html_mail)
        server.quit()
    else:
        print 'Local Notification: \n' + html_mail
