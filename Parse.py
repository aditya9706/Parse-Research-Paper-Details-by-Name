
# Project token:  ty2FpnXKEAqt
# API key:  	t-N_kGgKXHF4
# Raghu Vamsi : ngT8wRgAAAAJ&hl=en
# Shikha jain: qy2r8wsAAAAJ&hl=en
# Vikas saxena: lT3evUEAAAAJ&hl=en
from ph2 import ParseHub
import requests
import json
import re
import csv
import time
import pandas as pd

data = pd.read_csv("scholar_id.csv")
ids = data["id"]
print(ids,type(ids))
for k in range(len(ids)):
	if k%2 != 0:
		input_value = ids[k]
		params = {
		  "api_key": "t-N_kGgKXHF4",
		  "start_url": "https://scholar.google.co.in/citations?user="+input_value
		}

		r = requests.post('https://www.parsehub.com/api/v2/projects/ty2FpnXKEAqt/run', data=params)


		s1 = r.text
		x1 = json.loads(s1)
		print(x1['run_token'])
		run_token = x1['run_token']

		params = {
		  "api_key": "t-N_kGgKXHF4",
		}
		flag = 0

		while(flag == 0):
		    r1 = requests.get('https://www.parsehub.com/api/v2/runs/'+run_token, params = params)
		    s1 = r1.text
		    x1 = json.loads(s1)
		    flag = x1['data_ready']

		time.sleep(7)
		params = {
			'api_key': "t-N_kGgKXHF4",
			"format": "json"
		}
		r = requests.get('https://www.parsehub.com/api/v2/projects/ty2FpnXKEAqt/last_ready_run/data', params=params)
		s = r.text
		
		arr = [1,2,3,4]
		for i in arr:
			if i == 1:
				try:
					with open('scholars_'+input_value+'_conference.csv','w') as writeFile:
						writer = csv.writer(writeFile)
						writer.writerow(["Paper_Name","Total_cite_count","Publish_year","Authors","Publication_date","Conference","Pages","Publisher","cite_in_2000","cite_in_2001","cite_in_2002","cite_in_2003","cite_in_2004","cite_in_2005","cite_in_2006","cite_in_2007","cite_in_2008","cite_in_2009","cite_in_2010","cite_in_2011","cite_in_2012","cite_in_2013","cite_in_2014","cite_in_2015","cite_in_2016","cite_in_2017","cite_in_2018","cite_in_2019"])
						data = json.loads(s)
						count = 0
						flag = ""
						for i in range(len(data["Paper_name"])):

							paper_name = ""
							total_citation = ""
							publish_year = ""
							authors = ""
							publication_date = ""
							conference = ""
							pages = ""
							publisher = ""
							cite_value = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
							k = data["Paper_name"]
							# s = k[i]
							paper = k[i]
							paper_name = paper['name']
							if flag == paper_name:
								break
							if count == 0:
								flag = paper_name
								count += 1
							try:
								total_citation = paper['Total_citation']
							except KeyError:
								total_citation = ""	
							try:
								publish_year = paper['Published_year']
							except KeyError:
								publish_year = ""
							authors = paper['Authors']
							
							try:
								publication_date = paper['publicationDate']
							except KeyError:
								publication_date = ""

							try:
								conference = paper['Conference']
							except KeyError:
								conference = ""
							
							try:	
								pages = paper['pages']
							except KeyError:
								pages = ""

							try:
								publisher = paper['publisher']
							except KeyError:
								publisher = ""

							try:	
								citation = paper['Citation_count']
							except KeyError:
								citation = []
							for j in range(len(citation)):
								cite = citation[j]
								y = cite["url"]
								sp = (re.split(r'=',y))
								year = sp[-1]
								index = int(year[2:])
								cite_value[index] = cite['Cite']
							if conference != "":	
								writer.writerow([paper_name,total_citation,publish_year,authors,publication_date,conference,pages,publisher,cite_value[0],cite_value[1],cite_value[2],cite_value[3],cite_value[4],cite_value[5],cite_value[6],cite_value[7],cite_value[8],cite_value[9],cite_value[10],cite_value[11],cite_value[12],cite_value[13],cite_value[14],cite_value[15],cite_value[16],cite_value[17],cite_value[18],cite_value[19]])
					writeFile.close()
				except 	Exception:
					print("file already exists")		
			elif i == 2:
				try:
					with open('scholars_'+input_value+'_journal.csv','w') as writeFile:
						writer = csv.writer(writeFile)
						writer.writerow(["Paper_Name","Total_cite_count","Publish_year","Authors","Publication_date","Journal","Volume","Issue","Pages","Publisher","cite_in_2000","cite_in_2001","cite_in_2002","cite_in_2003","cite_in_2004","cite_in_2005","cite_in_2006","cite_in_2007","cite_in_2008","cite_in_2009","cite_in_2010","cite_in_2011","cite_in_2012","cite_in_2013","cite_in_2014","cite_in_2015","cite_in_2016","cite_in_2017","cite_in_2018","cite_in_2019"])
						data = json.loads(s)
						count = 0
						flag = ""
						for i in range(len(data["Paper_name"])):

							paper_name = ""
							total_citation = ""
							publish_year = ""
							authors = ""
							publication_date = ""
							# conference = ""
							pages = ""
							journal = ""
							volume = ""
							issue  = ""
							publisher = ""
							cite_value = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
							k = data["Paper_name"]
							# s = k[i]
							paper = k[i]
							paper_name = paper['name']
							if flag == paper_name:
								break
							if count == 0:
								flag = paper_name
								count += 1
							try:
								total_citation = paper['Total_citation']
							except KeyError:
								total_citation = ""	
							try:
								publish_year = paper['Published_year']
							except KeyError:
								publish_year = ""
							authors = paper['Authors']
							
							try:
								publication_date = paper['publicationDate']
							except KeyError:
								publication_date = ""

							try:
								journal = paper['Journal']
							except KeyError:
								journal = ""
							
							try:
								volume = paper['Volume']
							except KeyError:
								volume = ""

							try:
								issue = paper['Issue']
							except KeyError:
								issue = ""

							try:	
								pages = paper['pages']
							except KeyError:
								pages = ""

							try:
								publisher = paper['publisher']
							except KeyError:
								publisher = ""

							try:	
								citation = paper['Citation_count']
							except KeyError:
								citation = []
							for j in range(len(citation)):
								cite = citation[j]
								y = cite["url"]
								sp = (re.split(r'=',y))
								year = sp[-1]
								index = int(year[2:])
								cite_value[index] = cite['Cite']
							if journal != "":	
								writer.writerow([paper_name,total_citation,publish_year,authors,publication_date,journal,volume,issue,pages,publisher,cite_value[0],cite_value[1],cite_value[2],cite_value[3],cite_value[4],cite_value[5],cite_value[6],cite_value[7],cite_value[8],cite_value[9],cite_value[10],cite_value[11],cite_value[12],cite_value[13],cite_value[14],cite_value[15],cite_value[16],cite_value[17],cite_value[18],cite_value[19]])
					writeFile.close()
				except 	Exception:
					print("file already exists")
			elif i == 3:
				try:
					with open('scholars_'+input_value+'_BookChapter.csv','w') as writeFile:
						writer = csv.writer(writeFile)
						writer.writerow(["Paper_Name","Total_cite_count","Publish_year","Authors","Publication_date","Book_chapter","Pages","Publisher","cite_in_2000","cite_in_2001","cite_in_2002","cite_in_2003","cite_in_2004","cite_in_2005","cite_in_2006","cite_in_2007","cite_in_2008","cite_in_2009","cite_in_2010","cite_in_2011","cite_in_2012","cite_in_2013","cite_in_2014","cite_in_2015","cite_in_2016","cite_in_2017","cite_in_2018","cite_in_2019"])
						data = json.loads(s)
						count = 0
						flag = ""
						for i in range(len(data["Paper_name"])):

							paper_name = ""
							total_citation = ""
							publish_year = ""
							authors = ""
							publication_date = ""
							# conference = ""
							pages = ""
							book_chapter = ""
							publisher = ""
							cite_value = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
							k = data["Paper_name"]
							# s = k[i]
							paper = k[i]
							paper_name = paper['name']
							if flag == paper_name:
								break
							if count == 0:
								flag = paper_name
								count += 1
							try:
								total_citation = paper['Total_citation']
							except KeyError:
								total_citation = ""	
							try:
								publish_year = paper['Published_year']
							except KeyError:
								publish_year = ""
							authors = paper['Authors']
							
							try:
								publication_date = paper['publicationDate']
							except KeyError:
								publication_date = ""

							try:
								book_chapter = paper['Book']
							except KeyError:
								book_chapter = ""

							try:	
								pages = paper['pages']
							except KeyError:
								pages = ""

							try:
								publisher = paper['publisher']
							except KeyError:
								publisher = ""

							try:	
								citation = paper['Citation_count']
							except KeyError:
								citation = []
							for j in range(len(citation)):
								cite = citation[j]
								y = cite["url"]
								sp = (re.split(r'=',y))
								year = sp[-1]
								index = int(year[2:])
								cite_value[index] = cite['Cite']
							if book_chapter != "":	
								writer.writerow([paper_name,total_citation,publish_year,authors,publication_date,book_chapter,pages,publisher,cite_value[0],cite_value[1],cite_value[2],cite_value[3],cite_value[4],cite_value[5],cite_value[6],cite_value[7],cite_value[8],cite_value[9],cite_value[10],cite_value[11],cite_value[12],cite_value[13],cite_value[14],cite_value[15],cite_value[16],cite_value[17],cite_value[18],cite_value[19]])
					writeFile.close()
				except 	Exception:
					print("file already exists")
			elif i == 4:
				try:
					with open('scholars_'+input_value+'_book.csv','w') as writeFile:
						writer = csv.writer(writeFile)
						writer.writerow(["Paper_Name","Total_cite_count","Publish_year","Authors","Publication_date","Pages","Publisher","cite_in_2000","cite_in_2001","cite_in_2002","cite_in_2003","cite_in_2004","cite_in_2005","cite_in_2006","cite_in_2007","cite_in_2008","cite_in_2009","cite_in_2010","cite_in_2011","cite_in_2012","cite_in_2013","cite_in_2014","cite_in_2015","cite_in_2016","cite_in_2017","cite_in_2018","cite_in_2019"])
						data = json.loads(s)
						count = 0
						flag = ""
						for i in range(len(data["Paper_name"])):

							paper_name = ""
							total_citation = ""
							publish_year = ""
							authors = ""
							publication_date = ""
							# conference = ""
							pages = ""
							book_chapter = ""
							conference = ""
							journal = ""
							volume = ""
							publisher = ""
							cite_value = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
							k = data["Paper_name"]
							# s = k[i]
							paper = k[i]
							paper_name = paper['name']
							if flag == paper_name:
								break
							if count == 0:
								flag = paper_name
								count += 1
							try:
								total_citation = paper['Total_citation']
							except KeyError:
								total_citation = ""	
							try:
								publish_year = paper['Published_year']
							except KeyError:
								publish_year = ""
							authors = paper['Authors']
							
							try:
								publication_date = paper['publicationDate']
							except KeyError:
								publication_date = ""

							try:
								journal = paper['Journal']
							except KeyError:
								journal = ""

							try:
								book_chapter = paper['Book']
							except KeyError:
								book_chapter = ""

							try:
								conference = paper['Conference']
							except KeyError:
								conference = ""

							try:	
								pages = paper['pages']
							except KeyError:
								pages = ""

							try:
								publisher = paper['publisher']
							except KeyError:
								publisher = ""

							try:	
								citation = paper['Citation_count']
							except KeyError:
								citation = []
							for j in range(len(citation)):
								cite = citation[j]
								y = cite["url"]
								sp = (re.split(r'=',y))
								year = sp[-1]
								index = int(year[2:])
								cite_value[index] = cite['Cite']
							if conference == "" and book_chapter == "" and journal == "":	
								writer.writerow([paper_name,total_citation,publish_year,authors,publication_date,pages,publisher,cite_value[0],cite_value[1],cite_value[2],cite_value[3],cite_value[4],cite_value[5],cite_value[6],cite_value[7],cite_value[8],cite_value[9],cite_value[10],cite_value[11],cite_value[12],cite_value[13],cite_value[14],cite_value[15],cite_value[16],cite_value[17],cite_value[18],cite_value[19]])
					writeFile.close()
				except 	Exception:
					print("file already exists")
			elif i == 5:
				break