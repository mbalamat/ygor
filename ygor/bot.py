import hashlib, os, sys, urllib2, difflib
from bs4 import BeautifulSoup as bs

def open_config_file():
    with open('urls.conf', 'r') as file:
        urls = file.readlines()
    urls = [x.strip() for x in urls]
    return urls

def write_latest_file(filename, content):
    with open('./versions/' + filename, 'w') as f:
        f.write(str(content))

def load_remote_html(url):
    try:
        latest_html = urllib2.urlopen(url).read()
        latest_html = bs(latest_html, "html.parser")
        if len(latest_html) != 0:
            return latest_html
        else:
            return None
    except:
        return None

def load_local_html(url):
    filename = hashlib.sha256(url).hexdigest()
    if os.path.isdir('./versions/'):
        if os.path.isfile('./versions/' + filename):
            with open('./versions/' + filename, 'r') as local_html:
                current_html = local_html.readlines()
            current_html = ''.join(current_html)
            current_html = bs(current_html, "html.parser")
            return current_html
        else:
            print 'New site to monitor found, making local copy of the site...'
            write_latest_file(filename, load_remote_html(url))
            return None
    else:
        print 'Error: Versions directory doesn\'t exist\n"Making it ...'
        os.mkdir( './versions', 0755 )
        if os.path.isdir('./versions/'):
            print 'Done please rerun ygor'
            sys.exit()
        else:
            print 'There was a problem creating versions directory :('
            sys.exit(-1)

def check_diff(current_html, remote_html):
    diff = difflib.ndiff(str(current_html.prettify('utf-8')).splitlines(), str(remote_html.prettify('utf-8')).splitlines())
    additions = ''.join(x[2:] for x in diff if x.startswith('+ '))
    deletions = ''.join(x[2:] for x in diff if x.startswith('- '))
    if len(additions) == 0 and len(deletions) == 0:
        return False
    return True
