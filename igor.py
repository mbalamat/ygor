import bot, notify

receiver_address = os.environ['RECEIVER_ADDRESS']
urls = bot.open_config_file()

for url in urls:
    local_html = bot.load_local_html(url)
    if local_html == None:
        print 'New site added to ./versions'
        break
    latest_html = bot.load_remote_html(url)
    if bot.check_diff(local_html, latest_html):
        notify.notify('email', receiver_address, url)
        bot.write_latest_file(hashlib.sha256(url).hexdigest(), latest_html)
    else:
        print 'No changes found @ ' + url
        break
