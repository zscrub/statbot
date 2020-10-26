import requests, re
from bs4 import BeautifulSoup

url = 'https://www.espn.com/nfl/schedule'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

weekSchedule_elems = soup.find(id="global-viewport")
teamNames = weekSchedule_elems.find_all(class_="team-name")
teamMatchups1 = weekSchedule_elems.find_all(class_="odd")
teamMatchups2 = weekSchedule_elems.find_all(class_="even")

weekSchedule = teamMatchups1+teamMatchups2
bigStatList = []
teamMatchupList = []
matchups = []

for i in weekSchedule:
    bigStatList.append(i.text)
print(bigStatList)

for i in teamNames:
    teamMatchupList.append(i.text)

for i in range(len(teamMatchupList)):    
    if i%2==0:
        matchups.append([teamMatchupList[i], teamMatchupList[i+1]])
