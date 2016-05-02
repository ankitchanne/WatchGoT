from bs4 import BeautifulSoup
import requests, webbrowser
#show = raw_input()

html = requests.get("https://kat.cr/usearch/game%20of%20thrones/?field=seeders&sorder=desc")
#html = requests.get("https://kat.cr/usearch/"+show+"/?field=seeders&sorder=desc")
data = html.text
soup = BeautifulSoup(data,"html.parser")
links =  soup.find_all(class_= "icon16");

for i in links[1:2]:
	magnet = i.get('href')

webbrowser.get().open(magnet)

