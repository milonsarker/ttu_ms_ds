import requests as r
from bs4 import BeautifulSoup
import csv

urltoget = 'http://drd.ba.ttu.edu/sites/wowmobs/'
fp = '/home/isqsdac/Downloads/'
filename1 = 'dataout.csv'

res = r.get(urltoget)

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
                childres = r.get(urltoget + childhref)
                childsoup = BeautifulSoup(childres.content, 'lxml')
                mobinfo = childsoup.find('div', attrs={'id' : 'mobcard'}).find_all('span', attrs={'class' : 'val'})
                datawriter.writerow([mobid, mobinfo[0].text, quality, mobinfo[3].text])

