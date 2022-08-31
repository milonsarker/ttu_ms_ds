#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import pandas as pd

class Business_Intelligence:
	def explore_Webpages(self):
		data = requests.get('http://drd.ba.ttu.edu/isqs6339/imbadproducts/')
		#print(data.content)
		soup = BeautifulSoup(data.content, 'lxml')

		results = soup.find('a')
		#print(results)

		#print(results['href'])

		results = soup.find_all('a')
		for a in results:
			print(a['href'])

		results = soup.find_all('span', attrs = {'class' : 'productid'})
		for a in results:
			print(a.text)


		results = soup.find('div', attrs = {'id' : 'searchresults'})
		print(results)
	def scrap_and_prep_csv(self):
		url = 'http://drd.ba.ttu.edu/isqs6339/imbadproducts/'
		content_data = requests.get(url)
		if content_data.status_code == 200:
			print('Request URL is good')
		else:
			exit
		print(content_data.headers)
		soupObj = BeautifulSoup(content_data.content, 'lxml')
		
		product_result = soupObj.find_all('a')
		for prod in product_result:
			print(prod)
		print('_____________________________________________________________')
		searchResults = soupObj.find('div', attrs = {'id' : 'searchresults'})
		print(searchResults)
		print('_____________________________________________________________')
		prodResult = searchResults.find_all('a')

		data_output = []
		with open('scrapped_data.csv','w') as write_fh:
			for pr in prodResult:
				rec_dict = {}
				rec_dict['href'] = pr['href']
				rec_dict['prod_id'] = pr.find('span', attrs = {'class' : 'productid'}).text
				rec_dict['prod_title'] = pr.find('span', attrs = {'class' : 'producttitle'}).text
				rec_dict['prod_price'] = pr.find('span', attrs = {'class' : 'productprice'}).text
				rec_dict['pred_desc'] = pr.find('span', attrs = {'class' : 'productdesc'}).text
				data_output.append(rec_dict)
			print(data_output)


	def scrap_and_prep_csv_in_class_exmaple(self):
		url = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.1/gamers/'
		content_data = requests.get(url)
		if content_data.status_code == 200:
			#print('Request URL is good')
			pass
		else:
			exit
		soupObj = BeautifulSoup(content_data.content, 'lxml')
		gamers_data = soupObj.find('table')
		records = gamers_data.find_all('tr')
		data_list = []
		flag = True
		for rec in records: 
			if flag:
				row_data = rec.find_all('th')
				dr = []
				for a in row_data:
					dr.append(a.text)
				data_list.append(dr)
				flag = False
			else:
				row_data = rec.find_all('td')
				dr = []
				for a in row_data:
					url = a.find_all('a')
					if len(url) == 0:
						dr.append(a.text)
					else:
						try:
							dr.append(url[0]['href'])
						except Exception as e:
							dr.append([])
							print(e)
				data_list.append(dr)
		print(data_list)
	def home_Exercise_1(self):
		root_url = "http://drd.ba.ttu.edu/sites/extracker/"
		url_data = requests.get(root_url)
		True if url_data.status_code == 200 else exit
		soupObj = BeautifulSoup(url_data.content, 'lxml')
		tbl_data = soupObj.find('table')
		records = tbl_data.find_all('tr')
		data = []
		def same_task_one_func(records):
			for row in records:
				row_data = {}
				if len(row.find_all('td')) > 0:
					fields = row.find_all('td')
					url_link = fields[0].find('a')
					row_data['details_link'] = url_link['href']
					row_data['rank'] = fields[1].text
					row_data['name'] = fields[2].text
					row_data['avg_sleep'] = fields[3].text
					row_data['avg_water'] = fields[4].text
					row_data['avg_steps'] = fields[5].text
					row_data['metric'] = fields[6].text
					data.append(row_data)

		same_task_one_func(records)

		flag_dict = {'1':True}
		link_list = soupObj.find_all('a')
		for link in link_list:
			if 'index.php' in link['href'] and link.text not in flag_dict:
				print(link['href'])
				url = root_url + link['href']
				url_data = requests.get(url)
				soupObj = BeautifulSoup(url_data.content, 'lxml')
				tbl_data = soupObj.find('table')
				records = tbl_data.find_all('tr')
				same_task_one_func(records)
				flag_dict[link.text] = True
		print(flag_dict)
		df = pd.DataFrame(data)
		print(df)

if __name__=="__main__":
	bi_Obj = Business_Intelligence()
	#bi_Obj.explore_Webpages()
	#bi_Obj.scrap_and_prep_csv()
	#bi_Obj.scrap_and_prep_csv_in_class_exmaple()
	bi_Obj.home_Exercise_1()

