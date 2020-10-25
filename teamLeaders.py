import time
import sqlite3
import requests, re
from bs4 import BeautifulSoup

conn = sqlite3.connect('teamLeader_stats.db')
cursor = conn.cursor()

c1 = """CREATE TABLE IF NOT EXISTS
    teamLeaders(leaderStat_id INTEGER PRIMARY KEY, Team TEXT, Goal1 TEXT, Goal2 TEXT, Goal3 TEXT, Goal4 TEXT, Goal5 TEXT, 
    PassingLeader TEXT, RushingLeader TEXT, ReceivingLeader TEXT, TackleLeader TEXT, IntLeader TEXT, Score1 TEXT, Score2 TEXT, 
    Score3 TEXT, Score4 TEXT, Score5 TEXT)
"""

cursor.execute(c1)

teams = ["ari", "atl", "bal", "buf", "car", "chi", "cin", "cle", "dal", "den", "det",
         "gb", "hou", "ind", "jax", "kc", "lv", "lac", "lar", "mia", "min",
         "ne", "no", "nyg", "nyj", "phi", "pit", "sf", "sea", "tb", "ten", "wsh"
         ]

teamsDict = {"ari":"Arizona Cardinals", "atl": "Atlanta Falcons", "bal": "Baltimore Ravens", 
         "buf":"Buffalo Bills", "car":"Carolina Panthers", "chi":"Chicago Bears", 
         "cin":"Cincinnati Bengals", "cle":"Clevland Browns", "dal":"Dallas Cowboys",
         "den":"Denver Broncos", "det":"Detroit Lions",
         "gb":"Green Bay Packers", "hou":"Houston Texans", "ind":"Indianapolis Colts", 
         "jax":"Jacksonville Jaguars", "kc":"Kansas City Chiefs", "lv":"Los Vegas Raiders",
         "lac":"Los Angeles Chargers", "lar":"Los Angeles Rams", "mia":"Miami Dolphins", "min":"Minnesota Vikings",
         "ne":"New England Patriots", "no":"New Orleans", "nyg":"New York Giants", 
         "nyj":"New York Jets", "phi":"Philidelphia Eagles", "pit":"Pittsburgh Steelers",
         "sf":"San Fransisco 49ers", "sea":"Seattle Seahawks", "tb":"Tampa Bay Buccaneers",
         "ten":"Tennessee Titans", "wsh":"Washington Football Team"
         }

         
def getTeamLeaders():
    teamLeadersList = []
    for team in teams:
        url = "https://www.espn.com/nfl/team/stats/_/name/"+teams[teams.index(team)]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        stat_name = soup.find_all(class_='h8 mb2 clr-gray-03')
        player_name = soup.find_all(class_='di n8')
        number = soup.find_all(class_='clr-gray-01 pr3 hs2')
   
        allStats = []
        
        allStats.append(team)
        for s in stat_name:            
            allStats.append(s.text)
        for p in player_name:
            if str(p.text)[-1] != 'S':
                name = str(p.text)[:-2] + ' (' + str(p.text)[-2:] + ')'
            else:
                name = str(p.text)[:-1] + ' (' + str(p.text)[-1:] + ')'
            allStats.append(name)
        for n in number:            
            allStats.append(n.text)
        
        teamLeadersList.append(allStats)
    return teamLeadersList


def populateDB():
    print('populating database...')
    for statLists in getTeamLeaders():
        print('inserting {0}...'.format(statLists))
        cursor.execute("INSERT INTO teamLeaders (Team, Goal1, Goal2, Goal3, Goal4, Goal5, PassingLeader, RushingLeader, ReceivingLeader, TackleLeader, IntLeader, Score1, Score2, Score3, Score4, Score5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (statLists[0], statLists[1], statLists[2], statLists[3], statLists[4], statLists[5], statLists[6], statLists[7], statLists[8], statLists[9], statLists[10], statLists[11], statLists[12], statLists[13], statLists[14], statLists[15]))
        conn.commit()
        
def fetchDB():
    cursor.execute("SELECT * FROM teamLeaders")
    res = cursor.fetchall()
    return res


def updateDB():
    print('out with the old...')
    clearDB()
    print('fetching new data...')
    populateDB()
    print('done')
    # res = cursor.fetchall()
    # return res

def clearDB():
    print('clearing...')
    cursor.execute('DELETE FROM teamLeaders;')
    conn.commit()
    print('done')


# populateDB()
# print(fetchDB())
# clearDB()