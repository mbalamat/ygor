import bot

GREEN = '\033[92m'
RED = '\033[91m'
END = '\033[0m'

def print_with_color(outcome, string):
    if outcome:
        print GREEN + string + ' PASS' + END
    else:
        print RED + string + ' FAIL' + END

urls = bot.open_config_file()
print_with_color(urls[0] == 'https://mbalamat.site/test.html', 'open_config_file()')

latest_html = bot.load_remote_html(urls[0])
if latest_html is None:
    print_with_color(False, 'Getting page was not possible check internet connection or the case of an empty response!')
else:
    #print latest_html.prettify()
    #print len(latest_html)
    print_with_color(True, 'load_remote_html()')


if bot.check_diff(bot.load_remote_html('https://mbalamat.site/test.html'), bot.load_remote_html('https://mbalamat.site/test.html')) == False:
    print_with_color(True, 'check_diff(): Same sites as input')
else:
    print_with_color(False, 'check_diff(): Same sites as input')

if bot.check_diff(bot.load_remote_html('https://mbalamat.site/test.html'), bot.load_remote_html('https://mbalamat.site/test1.html')) == True:
    print_with_color(True, 'check_diff(): Different sites as input')
else:
    print_with_color(False, 'check_diff(): Different sites as input')

