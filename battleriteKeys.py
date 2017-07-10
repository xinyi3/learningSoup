import bs4 as bs
import urllib2
import unicodedata
import time
from random import randint
import smtplib
import re

set1 = {1}
### email notification
# server = smtplib.SMTP('smtp.live.com', 587)
# server.ehlo()
# server.starttls()
# server.login("yourEmail", "YourPassword")

listOfLinks = []

while(1):
    headers = { 'User-Agent' : 'battlerite lite keys bot 0.2' }

    req = urllib2.Request('https://www.reddit.com/r/BattleRite/search?q=key%7Clite&restrict_sr=on&sort=new&t=week', None, headers)

    battleriteSource = urllib2.urlopen(req).read()
    brSoup = bs.BeautifulSoup(battleriteSource, 'lxml')

    body = brSoup.find(class_="contents")

    for url in body.find_all('a'):
        postLink = url.get('href')
        if(postLink.count('comments')>0 and postLink.count('reddit.com')>0):
            if(postLink not in listOfLinks):
                listOfLinks.append(postLink)
            
    print('found ' + str(len(listOfLinks)) + " related posts")
    i=1
    # make function for this
    for link in listOfLinks:
        print('checking post number ' + str(i))
        i=i+1
        req1 = urllib2.Request(link, None, headers)
        postSource = urllib2.urlopen(req1).read()
        postSoup = bs.BeautifulSoup(postSource, 'lxml')
        postContent = postSoup.body

        for paragraph in postContent.find_all('p'):
            temp = paragraph.text
            matchObj = re.match(".{5}-.{5}-.{5}", temp, flags=0)
            if( matchObj and not(temp in set1)):
                set1.add(temp)
                print (temp)
                msg = temp
                # server.sendmail("toMailAccount", "FromMailAccount", msg.encode('utf-8'))
        time.sleep(randint(4,7))
        
    print('--------------------------------------------')
    
