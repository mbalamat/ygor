# Igor
![alt tag](http://www.asset1.net/tv/pictures/movie/igor-2008/Igor-18-1.jpg)

An html bot / assistant
###The problem:
Many students often forget to visit their school's / teacher's website and as a result they don't get informed about important tasks like homework, registration to a course, exam etc. and this problem affects their academic development.

###The solution:
Simple. A bot / assistant that checks web pages you are interested in and every time a change occurs, it notifies you.

---

###Installation:
* Prerequisites: pip (python's package manager), python 2.7

```
$ git clone https://github.com/mbalamat/igor
$ cd igor
$ pip install -r requirements.txt
```

* Set the environment variables used by igor:

```
$ export IGOR_EMAIL_ADDRESS='your@gmail.com'
$ export IGOR_EMAIL_PASSWD='yOuRp@ssWd'
$ export IGOR_RECEIVER_ADDRESS='your@gmail.com'
```

:point_up: Note that the gmail account that the bot will use to send emails has to enable less secure apps, you can to that [here] (https://www.google.com/settings/security/lesssecureapps).

:exclamation: You can not enable less secure apps if you have 2fa enabled. (Just create another gmail.)

* Set the urls you are interested in by changing the urls.conf file. Every line of the file corresponds to a url. Remove any blank lines.

:clap: :clap: :clap: You are all set.

Use igor.py with [CRON] (https://en.wikipedia.org/wiki/Cron) so it runs once every day or every time your computer reboots or whatever you want.
