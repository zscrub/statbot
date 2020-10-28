import requests, re
from bs4 import BeautifulSoup

teamRegions = ['Arizona', 'Atlanta', 'Baltimore', 'Buffalo', 'Carolina', 'Chicago', 
               'Cincinnati', 'Clevland', 'Dallas', 'Denver', 'Detroit', 'Green Bay',
               'Houston', 'Indianapolis', 'Jacksonville', 'Kansas City', 'Las Vegas',
               'L.A. Chargers',  'L.A. Rams', 'Miami', 'Minnesota', 'New England', 'New Orleans', 'N.Y. Giants', 
               'N.Y. Jets', 'Philidelphia', 'Pittsburgh', 'San Fransisco', 'Seattle',
               'Tampa Bay', 'Tennessee', 'Washington'  
]


def games():
    url = 'https://www.cbssports.com/nfl/schedule/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    matchup_elems = soup.find_all(class_="TableBase-bodyTd")

    # gameLeaders = soup.find_all(class_= '?') 

    matchupsList = []

    for i in matchup_elems:
        matchupsList.append(' '.join(i.text.split()))

    numOfGamesForTheWeek = len(matchupsList)/3

    n = 0
    bigList = [matchupsList[x:x+3] for x in range(0, len(matchupsList), 3)]

    # print(bigList)
    return bigList

print(games())