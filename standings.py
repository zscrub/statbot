import sqlite3
import requests, re
from bs4 import BeautifulSoup

# conn = sqlite3.connect('standings.db')
# cursor = conn.cursor()

# c1 = """CREATE TABLE IF NOT EXISTS
#     stats(stat_id INTEGER PRIMARY KEY, Team TEXT, Wins TEXT, Losses TEXT, Ties TEXT)
# """


url = "https://www.cbssports.com/nfl/standings/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

afcTeams = soup.find(id="TableBase-1")
afcTeam_elems = afcTeams.find_all('td')


nfcTeams = soup.find(id="TableBase-2")
nfcTeam_elems = nfcTeams.find_all('td')


def afcTeamStandings():
    afcTeamStandingList = []
    n = 0
    for i in afcTeam_elems:
        afcTeamStandingList.append(i.text.split())
    return afcTeamStandingList
# for i in nfcTeam_elems:
#     print(i.text[0])

def nfcTeamStandings():
    nfcTeamStandingList = []
    n = 0
    for i in nfcTeam_elems:
        nfcTeamStandingList.append(i.text.split())
    return nfcTeamStandingList


### AFC DIVISIONS ###

def afcEast():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in afcTeamStandings()[0:17]:
        seed1.append(i)
    for i in afcTeamStandings()[17:34]:
        seed2.append(i)
    for i in afcTeamStandings()[34:51]:
        seed3.append(i)    
    for i in afcTeamStandings()[51:68]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


def afcNorth():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in afcTeamStandings()[68:85]:
        seed1.append(i)
    for i in afcTeamStandings()[85:102]:
        seed2.append(i)
    for i in afcTeamStandings()[102:119]:
        seed3.append(i)    
    for i in afcTeamStandings()[119:136]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


def afcSouth():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in afcTeamStandings()[136:153]:
        seed1.append(i)
    for i in afcTeamStandings()[153:170]:
        seed2.append(i)
    for i in afcTeamStandings()[170:187]:
        seed3.append(i)    
    for i in afcTeamStandings()[187:204]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


def afcWest():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in afcTeamStandings()[204:221]:
        seed1.append(i)
    for i in afcTeamStandings()[221:238]:
        seed2.append(i)
    for i in afcTeamStandings()[238:255]:
        seed3.append(i)    
    for i in afcTeamStandings()[255:272]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


### NFC DIVISIONS ###

def nfcEast():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in nfcTeamStandings()[0:17]:
        seed1.append(i)
    for i in nfcTeamStandings()[17:34]:
        seed2.append(i)
    for i in nfcTeamStandings()[34:51]:
        seed3.append(i)    
    for i in nfcTeamStandings()[51:68]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


def nfcNorth():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in nfcTeamStandings()[68:85]:
        seed1.append(i)
    for i in nfcTeamStandings()[85:102]:
        seed2.append(i)
    for i in nfcTeamStandings()[102:119]:
        seed3.append(i)    
    for i in nfcTeamStandings()[119:136]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


def nfcSouth():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in nfcTeamStandings()[136:153]:
        seed1.append(i)
    for i in nfcTeamStandings()[153:170]:
        seed2.append(i)
    for i in nfcTeamStandings()[170:187]:
        seed3.append(i)    
    for i in nfcTeamStandings()[187:204]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4


def nfcWest():
    seed1 = []
    seed2 = []
    seed3 = []
    seed4 = []

    for i in nfcTeamStandings()[204:221]:
        seed1.append(i)
    for i in nfcTeamStandings()[221:238]:
        seed2.append(i)
    for i in nfcTeamStandings()[238:255]:
        seed3.append(i)    
    for i in nfcTeamStandings()[255:272]:
        seed4.append(i)    
    return seed1, seed2, seed3, seed4
# print(afcTeamStandings())
