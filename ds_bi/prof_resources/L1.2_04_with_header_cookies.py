import requests as r
from bs4 import BeautifulSoup
import csv
import time as t
import random as rnd

urltoget = 'http://drd.ba.ttu.edu/sites/wowmobs/'
fp = '/home/isqsdac/Downloads/'
filename1 = 'dataout.csv'
header = {'user_agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}
cookies = ""
lowval=3
highval=5

res = r.get(urltoget, headers=header)
cookies = res.cookies
soup = BeautifulSoup(res.content, 'lxml')

mobs = soup.find('div', attrs={'id' : 'mobindex'}).find_all('tr')

with open(fp + filename1, 'w') as dataout:
    datawriter = csv.writer(dataout, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    #write header row
    datawriter.writerow(['mobId', 'name', 'quality', 'level'])
    for m in mobs:
        td = m.find_all('td')
        if len(td) == 2:
            childhref = td[0].find('a')['href']
            mobid = childhref.split('=')[1]
            if mobid != '':
                quality = td[1].text
                childres = r.get(urltoget + childhref, headers=header, cookies=cookies)
                cookies = childres.cookies
                childsoup = BeautifulSoup(childres.content, 'lxml')
                mobinfo = childsoup.find('div', attrs={'id' : 'mobcard'}).find_all('span', attrs={'class' : 'val'})
                datawriter.writerow([mobid, mobinfo[0].text, quality, mobinfo[3].text])

                timetosleep = rnd.randint(lowval, highval) + rnd.random()
                t.sleep(timetosleep)
