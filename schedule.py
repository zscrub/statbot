import requests, re
from bs4 import BeautifulSoup

url = 'https://www.espn.com/nfl/scoreboard'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

date = soup.find_all(class_='date-heading js-show')
matchups = soup.find_all(class_='sb-team-short')

d = soup.find_all('span')

for i in d:
    print(i.text)
