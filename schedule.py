import requests, re
from bs4 import BeautifulSoup

url = 'https://www.espn.com/nfl/scoreboard'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# date = soup.find_all(class_='date-heading js-show')
m = soup.find(id='teams')
matchups = m.find_all(class_='sb-score-live')
*
print(m)
