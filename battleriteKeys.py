import bs4 as bs
import urllib2
import unicodedata
import time
from random import randint
import smtplib

set1 = {1}
# email notification
server = smtplib.SMTP('smtp.live.com', 587)
server.ehlo()
server.starttls()
server.login("yourEmail", "YourPassword")

while(1):
    headers = { 'User-Agent' : 'battlerite lite keys bot 0.1' }

    req = urllib2.Request('https://www.reddit.com/r/BattleRite/search?q=key%7Clite&restrict_sr=on&sort=new&t=hour', None, headers)

    battleriteSource = urllib2.urlopen(req).read()
    brSoup = bs.BeautifulSoup(battleriteSource, 'lxml')

    body = brSoup.find(class_="listing search-result-listing")

    for paragraph in body.find_all('p'):
        temp = paragraph.text
        if(temp.count('-')>1 and not(temp in set1)):
            set1.add(temp)
            print (temp)
            msg = temp
            # server.sendmail("toMailAccount", "FromMailAccount", msg.encode('utf-8'))

    print('--------------------------------------------')
    time.sleep(randint(4,7))
