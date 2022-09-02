'''
This code has been written in Ubuntu - Linux Environment. Hence, below  line has been added as shebang, means it'll be executed in python3. 
In this environment, python3 is located in /usr/bin/ directory. 
To run this code in any editor like Pycharm, Spyder etc, shebang should be removed. 
'''
#!/usr/bin/python3

'''
Packages: Two packages has been imported which are required to complete instructed tasks. 
'''
import requests
from bs4 import BeautifulSoup

'''
Class Definition : Program has been written in OOP manner. here is the below class: Business_Intelligence definition
'''
class Business_Intelligence:
	'''
	Function Name 	: 
	Parameters	: no parameters
	Purpose		: It has been designed to scrap data from certain URL and subsequently from child pages as per instructions. 
	'''	
	def task_3(self, url):
		print("\n***Task #3***")
		iphone_data = requests.get(url)
		soupObj = BeautifulSoup(iphone_data.content, 'lxml')
		fin_model = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find('td').text
		fin_storage = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find_all('td')[1].text
		print(fin_model + fin_storage)
		camera_feature = soupObj.find('div', attrs = {'id' : 'Phoneotherstuff'}).find('span', attrs = {'class' : 'item'}).find_all('li')
		data = [i.text for i in camera_feature]
		print("Front Camera Features: " + ",".join(data))
	def part_of_task_4(self, url, color, os):
		iphone_data = requests.get(url)
		soupObj = BeautifulSoup(iphone_data.content, 'lxml')
		fin_storage = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find_all('td')[0].text + \
			      soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find_all('td')[1].text
		fin_net = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[2].find_all('td')[0].text + \
			  soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[2].find_all('td')[1].text
		fin_dim = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[0].find_all('td')[0].text + \
			  soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[0].find_all('td')[1].text
		print(fin_net + '\n' + fin_storage + '\n' + color + '\n' + os + '\n' + fin_dim + '\n')
	'''
	Function Name 	: lab_one
	Parameters	: no parameters
	Purpose		: It has been designed to scrap data from certain URL and subsequently from child pages as per instructions. 
	'''	
	def lab_one(self):
		root_url = "http://drd.ba.ttu.edu/isqs6339/labs/lab1/"
		root_url_data = requests.get(root_url)
		print("Values for Task #1")
		print("Status Code of Call:  " + str(root_url_data.status_code))
		print("Page is Redirecting:  " + str(root_url_data.is_redirect))
		print("Current Page Encoding:  " + root_url_data.encoding)
		print("Returned Header for Page:  " + str(root_url_data.headers))

		soup_obj = BeautifulSoup(root_url_data.content, 'lxml')
		print("\n***Task #2***\nThe following are values for the IPhone 11 Pro")
		get_li_class = soup_obj.find('ul').find_all('li', attrs = {'class' : 'root'})
		for a in get_li_class:
			if a.find('span').text == "iPhone 11 Pro":
				print(a.find_all('li')[1].text)
				print(a.find_all('li')[0].text)
				iphone_url = root_url + a.find_all('li')[2].find('a')['href']
				self.task_3(iphone_url)
		print('\n***Task #4***')
		cnt = 1
		for a in get_li_class:
			print("***Phone #" + str(cnt) + " ***")
			print("Product Name: " + a.find('span').text)
			child_full_url = root_url + a.find_all('li')[2].find('a')['href']
			self.part_of_task_4(child_full_url, a.find_all('li')[1].text, a.find_all('li')[0].text)
			cnt += 1
'''
Function Name	: main
Parameters	: none
Brief Intro	: Code has been writen in OOP manner. Here, object of class Business_Intelligence will be created and relevant function will be called to complete 
		  required task
'''
if __name__=="__main__":
	bi_Obj = Business_Intelligence()
	bi_Obj.lab_one()
