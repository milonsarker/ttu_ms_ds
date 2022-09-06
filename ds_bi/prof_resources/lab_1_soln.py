import requests as r
from bs4 import BeautifulSoup

url = 'http://drd.ba.ttu.edu/isqs6339/labs/lab1/'

res = r.get(url)

#task 1
print()
print('Values for Task #1')
print('Status Code of Call:  ', res.status_code)
print('Page is Redirecting:  ', res.is_redirect)
print('Current Page Encoding:  ', res.encoding)
print('Returned Header for Page:  ', res.headers)


#task 2

soup = BeautifulSoup(res.content, 'lxml')

plist = soup.find('div', attrs={'id' : 'phonelist'})
iphone = plist.find('ul').find_all('li', attrs={'class' : 'root'})[1]
iphone_attr = iphone.find('ul').find_all('li')
print('\n***Task #2***')
print('The following are values for the IPhone 11 Pro')
print('OS:  ', iphone_attr[1].text.split(':  ')[1])
print('Color:  ', iphone_attr[0].text.split(':  ')[1])


#task 3

soup = BeautifulSoup(res.content, 'lxml')

plist = soup.find('div', attrs={'id' : 'phonelist'})
iphone = plist.find('ul').find_all('li', attrs={'class' : 'root'})[1]
iphone_attr = iphone.find('ul').find_all('li')

iphone_attr[2].find('a')['href']

res_child = r.get(url + iphone_attr[2].find('a')['href'])

child_soup = BeautifulSoup(res_child.content, 'lxml')

child_phone = child_soup.find('div', attrs={'id' : 'phonestuff'})

features = ''
front_features = child_phone.find('div', attrs={'id' : 'Phoneotherstuff'}).find_all('span', attrs={'class' : 'item'})[0]

for f in front_features.find_all('li'):
    features += f.text + ', '

print('\n***Task #3***')
print('Storage:  ', child_phone.find('div', attrs={'id' : 'Phoneinitial'}).find_all('td')[3].text)
print('Front camera Features:  ', features[:-2])


#task 4

soup = BeautifulSoup(res.content, 'lxml')

plist = soup.find('div', attrs={'id' : 'phonelist'})
plist = plist.find('ul').find_all('li', attrs={'class' : 'root'})

print('***Task #4***\n')
print('Here is your list of Phones:  \n')

#'product_name,network,storage,color,os,product_size\n')

counter = 1
    
for p in plist:
    pattr = p.find('ul').find_all('li')
    res_child = r.get(url + pattr[2].find('a')['href'])
    child_soup = BeautifulSoup(res_child.content, 'lxml')
    child_phone = child_soup.find('div', attrs={'id' : 'phonestuff'})

    print('*** Phone #' + str(counter) + ' ***')
    print('Product Name: ', p.find('span').text)
    print('Network: ', child_phone.find('div', attrs={'id' : 'Phoneinitial'}).find_all('td')[5].text)
    print('Storage: ', child_phone.find('div', attrs={'id' : 'Phoneinitial'}).find_all('td')[3].text)
    print('Color: ', pattr[1].text.split(':  ')[1])
    print('OS: ', pattr[0].text.split(':  ')[1])
    print('Product Size: ', child_phone.find('div', attrs={'id' : 'Phoneinitial'}).find_all('td')[1].text, '\n')
    counter += 1
    
    
