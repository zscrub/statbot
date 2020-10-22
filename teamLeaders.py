import requests, re
from bs4 import BeautifulSoup

teams = ["ari", "atl", "bal", "buf", "car", "chi", "cin", "cle", "dal", "den", "det",
         "gb", "hou", "ind", "jax", "kc", "lv", "lac", "lar", "mia", "min",
         "ne", "no", "nyg", "nyj", "phi", "pit", "sf", "sea", "tb", "ten", "wsh"
         ]

    
def getTeamLeaders():
    teamLeadersList = []
    for team in teams:
        leaderList = []
        url = "https://www.espn.com/nfl/team/stats/_/name/"+teams[teams.index(team)]
        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        playerStats = soup.find(class_='StatLeaders flex')
        playerStats_elems = playerStats.find_all('a')
        
        for stats in playerStats_elems:
            leaderList.append(str(stats.text))
        teamLeadersList.append(leaderList)

    return teamLeadersList

# if getTeamLeaders()[0][-1][:13] == "Interceptions":
#     print(getTeamLeaders()[0][-1][:getTeamLeaders()[0][-1].find('Interceptions')+1])


# print(getTeamLeaders()[0][0])