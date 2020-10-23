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
        queu_list = []

        url = "https://www.espn.com/nfl/team/stats/_/name/"+teams[teams.index(team)]
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        number = soup.find(class_='clr-gray-01 pr3 hs2')
        player_name = soup.find(class_='di n8')
        stat_name = soup.find(class_='h8 mb2 clr-gray-03')

        queu_list = stat_name.text, player_name.text, number.text
        teamLeadersList.append(queu_list)
    return teamLeadersList

print(getTeamLeaders()[0][0])
