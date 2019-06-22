import requests
from bs4 import BeautifulSoup
import string

paginas = int(input("Write how many pages do you want to i look for IP's (1 Page = 15 IP's): "))
pag = []
classes = []
classes_ = []
i = 0
while i < paginas:
	pag.extend(requests.get("https://www.gametracker.com/search/?&searchpge=%d#search" % (i)))
	i=i+1
pagstr=("\n".join(map(str,pag)))

for a in range(0,paginas,1):
	soup = BeautifulSoup(pagstr,'html.parser')
	for element in soup.find_all("span", class_="ip"):
		classes.append(element)
for classe in classes:
    classes_.extend(classe)
f= open("ips.txt","w+")
for x in range(len(classes_)):
    f.write(classes_[x])
    f.write('\n')
    for line in f.readlines():
        string.replace(line, "'b'",'')
        string.replace(line, "b'",'')

    
