import requests, re
from bs4 import BeautifulSoup

url = 'https://www.cbssports.com/nfl/schedule/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

def games():
    matchup_elems = soup.find_all(class_="TableBase-bodyTd")

    ## Get Week #

    matchupsList = []

    for i in matchup_elems:
        matchupsList.append(' '.join(i.text.split()))

    numOfGamesForTheWeek = len(matchupsList)/3

    n = 0
    bigList = [matchupsList[x:x+3] for x in range(0, len(matchupsList), 3)]

    # print(bigList)
    return bigList