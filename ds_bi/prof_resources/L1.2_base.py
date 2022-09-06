import requests as r
from bs4 import BeautifulSoup
import csv

urltoget = 'http://drd.ba.ttu.edu/sites/wowmobs/'

res = r.get(urltoget)

soup = BeautifulSoup(res.content, 'lxml')

mobs = soup.find('div', attrs={'id' : 'mobindex'}).find_all('tr')

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
            print('mobId:  ', mobid)
            print('name:  ', mobinfo[0].text)
            print('Quality:  ', quality)
            print('Level:  ', mobinfo[3].text)
            print('-----------------------')

