import bot, notify, os, hashlib, sys

try:
    receiver_address = os.environ['RECEIVER_ADDRESS']
except:
    print 'Set env variable RECEIVER_ADDRESS to the email address you want to send the alerts.'
    sys.exit(1)

urls = bot.open_config_file()

for url in urls:
    print 'checking url: ' + url
    local_html = bot.load_local_html(url)
    if local_html == None:
        print 'New site added to ./versions'
    else:
        latest_html = bot.load_remote_html(url)
        if latest_html == None:
            print 'Getting page was not possible, check internet connection or the case of an empty response!'
            #rerun igor maybe after some time?
        else:
            if bot.check_diff(local_html, latest_html):
                notify.notify('email', receiver_address, url)
                bot.write_latest_file(hashlib.sha256(url).hexdigest(), latest_html)
            else:
                print 'No changes found @ ' + url
