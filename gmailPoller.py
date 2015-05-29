import imaplib
import email
import smtplib
import time
import sys
import json
import urllib2
from pprint import pprint

if len(sys.argv) < 2:
    print "Usage: python gmailPoller.py <config_file.json>"
    sys.exit()

with open(sys.argv[1]) as configFile:
    config = json.load(configFile)

senders = []

def wakeTheImp(config):
    print 'Waking the imp at URL: %s' % config["url"]
    response = urllib2.urlopen(config["url"])
    output = response.read()
    #print 'URL output %s' % output
    if output == "OK":
        print "The imp was successfully woken"
    else:
        print "Error waking the imp: %s" % output

def checkForEmails(config):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(config["username"], config["password"])
    #mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    result, data = mail.uid('search', None, '(HEADER Subject "'+config["searchString"]+'" UNSEEN)') # search and return uids instead
#    print str(result)
#    print str(data)
    if len(data) > 0 and len(data[0]) > 0:
        print "New message found..."
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        
        wakeTheImp(config)

    mail.close()
    mail.logout()

    
while True:
    checkForEmails(config)
    time.sleep(10)
