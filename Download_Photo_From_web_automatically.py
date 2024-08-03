

import requests
import wget
from bs4 import BeautifulSoup

def download_image_from_web(url):
	res=requests.get(url)
	if res.status_code==200:
		data_text=res.text
		soup = BeautifulSoup(data_text, 'html.parser')
		i_na=0 #to name file if alt doesnt exist
		i=1
		for line in soup.prettify().split('\n'):
			#print(line)
			if "img" in line and "src" in line:
				#print(line)
				new_text=line.split('src="')[1].split('"')[0]
				if "alt" in line:
					name=line.split('alt="')[1].split('"')[0]+"."+line.split('.')[-1].split('"')[0]
				else:
					i_na+=1
				name=str(i_na)+"."+line.split('.')[-1].split('"')[0]
				#print(new_text,name)
				dow=wget.download(new_text,out="/storage/emulated/0/web_Photo/"+name)#This will download the file
				print(dow,f"{i}")
				i+=1
	else:
		print(f"you have some error {res.status_code}")
 
	
if __name__=="__main__":
	download_image_from_web("https://www.imdb.com/poll/t_64cN6dzPI/results")


