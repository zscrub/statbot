import sqlite3
import requests, re
from bs4 import BeautifulSoup

conn = sqlite3.connect('football_stats.db')
cursor = conn.cursor()

c1 = """CREATE TABLE IF NOT EXISTS
    stats(stat_id INTEGER PRIMARY KEY, Goal TEXT, Name TEXT, Score TEXT)
"""

cursor.execute(c1)

url = "https://www.pro-football-reference.com/leaders/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="div_yearly_leaders")
stat_elems = results.find_all('div', class_='tabular_row')
yearlyLeaderArr = []

for stats in stat_elems:
    arr = []
    for i in stats:
        try:
            string_stats = str(i)
            number = re.search("\((.*?)\)", string_stats)
            #print(number[1])
            arr.insert(-1, str(number[1]))
        except:
            test = str(i)
            if "tied" in test:
                #print(i)
                arr.insert(-1, str(i))

            else:
                pass

    strong_elem = stats.find('strong')
    a_href_elem = stats.find('a')
        
    arr.insert(0, str(strong_elem.text+":"))
    #print(strong_elem.text)
    
    if a_href_elem != None:
        #print(a_href_elem.text)
        arr.insert(1, str(a_href_elem.text))
    else:
        pass
    if 'div' in arr[-1]:
        x = str(arr[-1])
        x = (x.replace('<div>', ' '))
        x = (x.replace('</div>', ' '))
        arr[-1] = x
    # print(arr)    
    yearlyLeaderArr.append(arr)
            # [[type, name, team, number], [type, name, team, number]]


def populateDB():
    for statLists in yearlyLeaderArr:
        if len(statLists) == 3:
            cursor.execute("INSERT INTO stats (Goal, Name, Score) VALUES (?, ?, ?)", (statLists[0], statLists[1], statLists[2]))
            conn.commit()
        else:        
            cursor.execute("INSERT INTO stats (Goal, Score) VALUES (?, ?)", (statLists[0], statLists[1]))
            conn.commit()

def fetchDB():
    cursor.execute("SELECT * FROM stats")
    res = cursor.fetchall()
    return res


#### Passing stat function to return list (EMBEDDED MESSAGE) ###
def passingStatsList():
    returnList = []
    passGoals = ["Passes Completed:", "Pass Attempts:", "Passing Yds:", "Passing TD:", "Passer Rating:", "Long Pass:", "Passes Intercepted:", 
                 "Sacked:", "Sacked Yds Lost:", "Pick Sixes:", "Passing Yds/Game",  "Yds/Pass Att:", "Yds/Pass Cmp:", "Pass Attempts/Game",
                 "Adj Yds/Pass Att:", "Net Yds/Pass Att:", "Adj Net Yds/Pass Att:", "Passes Completed/Game:", "Pass Completion %:", "Pass Intercept. %:",
                 "Passing TD %:", "Sack %:", "QBR:", "Game-Winning Drives:"]   
    
    for i in fetchDB():
        # print(i)
        if i[1] in passGoals:
            if i[2] != None:
                returnList.append([i[1], i[2], i[3]])
            if i[2] == None:
                returnList.append([i[1], i[3]])
    return returnList


### Rushing stat function to return list (EMBEDDED MESSAGE) ###

def rushingStatsList():
    returnList = []
    rushGoals = ["Rushing Att:", "Rushing Yds:", "Rushing TD:", "Long Rush:", "Yds/Rushing Att:", "Rushing Yds/Game:", "Receptions:", 
                 "Receiving Yds:", "Receiving TD:", "Long Reception:", "Yds/Reception:",  "Receiving Yds/Game:", "Touchdowns:", "Rushing/Receiving TD:",
                 "Yds From Scrimmage:", "All-Purpose Yds:", "Total Offense:", "Touches:", "Yds/Touch:", "Kick Return Yds:", "Kick Return TD:", "Long Kick Return:",
                 "Yds/Kick Return:", "Punt Return Yds:", "Long Punt Return:", "Yds/Punt Return:"]   
    for i in fetchDB():
        if i[1] in rushGoals:
            if i[2] != None:
                returnList.append([i[1], i[2], i[3]])
            if i[2] == None:
                returnList.append([i[1], i[3]])
    return returnList


### Defensive Teams stat function to return list (EMBEDDED MESSAGE) ###

def defensiveStatsList():
    returnList = []
    defensiveGoals = ["Fumbles Recovered:", "Fumble Return Yds:", "Fumble Return TD:", "Interceptions:", "Intercept. Ret. Yds:", "Intercept. Ret. TD:", 
                      "Long Intercep. Return:", "Tackles Solo:", "Tackles Combined:", "Tackles For Loss:", "Fumbles Forced:",  "Passes Defended:", "Sacks:", 
                      "Safeties:"]
    for i in fetchDB():
        if i[1] in defensiveGoals:
            if i[2] != None:
                returnList.append([i[1], i[2], i[3]])
            if i[2] == None:
                returnList.append([i[1], i[3]])
    return returnList    


### Special Teams stat function to return list (EMBEDDED MESSAGE) ###

def specialTeamsStatsList():
    returnList = []
    specialTeamGoals = ["Extra Pt Made:", "Extra Pt Att:", "Total Field Goals Made:", "Field Goals Att:", "Field Goal %:", "Punts:", "Punting Yds:", 
                 "Long Punt:", "Punts Blocked:", "Yds/Punt:"]   
    for i in fetchDB():
        if i[1] in specialTeamGoals:
            if i[2] != None:
                returnList.append([i[1], i[2], i[3]])
            if i[2] == None:
                returnList.append([i[1], i[3]])
    return returnList
    
### set up update function >:( 
def clearDB():
    cursor.execute("DELETE FROM stats;")
    conn.commit()

clearDB()    
populateDB()

print(passingStatsList())

# print(res)
