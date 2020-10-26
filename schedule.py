import requests, re
from bs4 import BeautifulSoup

url = 'https://www.cbssports.com/nfl/schedule/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

weekSchedule_elems = soup.find(class_="Page-colMain")
teamNames = weekSchedule_elems.find_all(class_="TeamName")
## Get Result
r = weekSchedule_elems.find('a href')

## Get Week #

matchups = []

for i in teamNames:
    matchups.append(i.text)
    
print(r.text)
