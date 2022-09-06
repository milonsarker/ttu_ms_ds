#Request Library
import requests as r
from bs4 import BeautifulSoup

urltoget = 'http://drd.ba.ttu.edu/isqs6339/imbadproducts/'

res = r.get(urltoget)
res.content

#parse content into an object
soup = BeautifulSoup(res.content,'lxml')

#Find the first anchor links
results = soup.find("a")
print(results)
#pull the href
print(results['href'])

#Let's find all the anchor links
results = soup.find_all("a")

#Loop to see the links
for l in results:
    print(l['href'])
    
#How do we get the inner text
#note, this will strip all HTML tags
#That's great, but those are different fields
for l in results:
    print(l.text)    
    
#Let's parse by css class and retrieve the productIds
results = soup.find_all('span', attrs={'class' : 'productid'})
for l in results:
    #print(l) #returns HTML of each found node
    print(l.text)
    
#Let's return the prices
results = soup.find_all('span', attrs={'class' : 'productprice'})
for l in results:
    #print(l) #returns HTML of each found node
    print(l.text)

#How do we search by ID of a tag    
results = soup.find('div', attrs={'id' : 'searchresults'})
print(results)
