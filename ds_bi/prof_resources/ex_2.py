import requests as r
from bs4 import BeautifulSoup
import csv

urltoget = 'http://drd.ba.ttu.edu/isqs6339/imbadproducts/'

res = r.get(urltoget)

#Check if we have a good request
if res.status_code == 200:
    print('request is good')
else:
    print('bad request, received code ' + str(res.status_code))
    
#Let's look at the server header
print(res.headers)    

#Let's identify our products blocks in HTML
soup = BeautifulSoup(res.content,'lxml')

product_result = soup.find_all('a')
for pr in product_result:
    print(pr)
    
#WAIT!  What if another anchor was added to the page?
#As in the footer???
#Let's look at nested searches
#Note, the "searchresults" div
    
search_results = soup.find('div', attrs={'id' : 'searchresults'})

#Now, search for anchors within that result
product_result = search_results.find_all('a')    
for pr in product_result:
    print(pr)
    
#Let's print out each part for each item    
product_result = search_results.find_all('a')    
for pr in product_result:
    print('URL:  ' + pr['href'])
    print('Product ID:  ' + pr.find('span', attrs={'class' : 'productid'}).text)
    print('Product Title:  ' + pr.find('span', attrs={'class' : 'producttitle'}).text)
    print('Product Price:  ' + pr.find('span', attrs={'class' : 'productprice'}).text)
    print('Product Description:  ' + pr.find('span', attrs={'class' : 'productdesc'}).text)
    print('----------------')
    

