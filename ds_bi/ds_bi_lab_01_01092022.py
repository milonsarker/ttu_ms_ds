#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Business_Intelligence:
	def lab_one(self):
		def task_3(url):
			print("***Task #3***")
			iphone_data = requests.get(url)
			soupObj = BeautifulSoup(iphone_data.content, 'lxml')
			fin_model = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find('td').text
			fin_storage = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find_all('td')[1].text
			print(fin_model + fin_storage)
			camera_feature = soupObj.find('div', attrs = {'id' : 'Phoneotherstuff'}).find('span', attrs = {'class' : 'item'}).find_all('li')
			data = [i.text for i in camera_feature]
			print("Front Camera Features: " + ",".join(data))

		def part_of_task_4(url, color, os):
			iphone_data = requests.get(url)
			soupObj = BeautifulSoup(iphone_data.content, 'lxml')
			fin_storage = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find_all('td')[0].text + \
					soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[1].find_all('td')[1].text
			fin_net = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[2].find_all('td')[0].text  \
				 + soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[2].find_all('td')[1].text
			fin_dim = soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[0].find_all('td')[0].text + \
					soupObj.find('div', attrs = {'id' : 'Phoneinitial'}).find_all('tr')[0].find_all('td')[1].text

			print(fin_net)
			print(fin_storage)
			print(color)
			print(os)
			print(fin_dim)



		root_url = "http://drd.ba.ttu.edu/isqs6339/labs/lab1/"
		root_url_data = requests.get(root_url)
		print("Values for Task #1")
		print("Status Code of Call:  " + str(root_url_data.status_code))
		print("Page is Redirecting:  " + str(root_url_data.is_redirect))
		print("Current Page Encoding:  " + root_url_data.encoding)
		print("Returned Header for Page:  " + str(root_url_data.headers))

		soup_obj = BeautifulSoup(root_url_data.content, 'lxml')
		print("***Task #2***\nThe following are values for the IPhone 11 Pro")
		get_ul = soup_obj.find('ul')
		get_li_class = get_ul.find_all('li', attrs = {'class' : 'root'})

		cnt = 1

		for a in get_li_class:
			if a.find('span').text == "iPhone 11 Pro":
				print(a.find_all('li')[1].text)
				print(a.find_all('li')[0].text)
				iphone_url = root_url + a.find_all('li')[2].find('a')['href']
				task_3(iphone_url)
		for a in get_li_class:
			print("***PHone #"+str(cnt)+ " ***")
			print("Product Name: "+ a.find('span').text)
			iphone_url = root_url + a.find_all('li')[2].find('a')['href']
			part_of_task_4(iphone_url, a.find_all('li')[1].text, a.find_all('li')[0].text)
			cnt += 1
if __name__=="__main__":
	bi_Obj = Business_Intelligence()
	bi_Obj.lab_one()

