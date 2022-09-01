import requests as r
from bs4 import BeautifulSoup

searchURL = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.2/search.php'

res = r.get(searchURL)
soup = BeautifulSoup(res.content,'lxml')
res.content
ddlresult = soup.find("select", attrs={'id' : 'ddlRandomness'})

for o in ddlresult.find_all('option'):
    print(o['value'])
