import smtplib, os

try:
    email_address = os.environ['EMAIL_ADDRESS']
    email_passwd = os.environ['EMAIL_PASSWD']
except:
    print 'Env variables not set please set EMAIL_ADDRESS and EMAIL_PASSWD.'

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
