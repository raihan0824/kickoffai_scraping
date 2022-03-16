from selenium import webdriver    # to  control the chrome browser
import time
from bs4 import BeautifulSoup     # to parse the page source
import pandas as pd                # to create csv file of scraped user details
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re
import json
import time

url = 'https://kickoff.ai/matches'
options = Options()
options.add_argument("user-data-dir=/Users/raihanafiandi/Library/Application Support/Google/Chrome/Default")
driver = webdriver.Chrome(chrome_options=options)    # creating chrome instance
driver.get(url)
time.sleep(3)
while True:
    try:
        show_more = driver.find_element_by_xpath("//button[text()='Show more']")
        driver.execute_script("arguments[0].click();", show_more)
        time.sleep(2)
    except:
        print('No more show more button')
        break
time.sleep(3)
ss = driver.page_source
soup=BeautifulSoup(ss,'html.parser') 
time.sleep(1)

DATE=[]
HOME=[]
AWAY=[]
HOME_GOAL=[]
AWAY_GOAL=[]
HOME_WIN=[]
DRAW_WIN=[]
AWAY_WIN=[]
HOME_KICK_SCORE=[]
AWAY_KICK_SCORE=[]

for link in links:
    soup = BeautifulSoup(urlopen(link),'html.parser')
    DATE.append(soup.find('div',{"class":"match-time"}).text.strip()) # DATE
    HOME.append(soup.find('div',{"class":"team-home"}).text.strip()) # HOME
    AWAY.append(soup.find('div',{"class":"team-away"}).text.strip()) # AWAY
    HOME_GOAL.append(soup.find('div',{"class":"result"}).text.strip()[0]) # HOME_GOAL
    AWAY_GOAL.append(soup.find('div',{"class":"result"}).text.strip()[4]) # AWAY_GOAL
    HOME_WIN.append(soup.find('span',{"class":"prediction-win-home"}).text.strip()) # HOME_WIN
    DRAW_WIN.append(soup.find('span',{"class":"prediction-draw text-muted"}).text.strip()) # DRAW_WIN
    AWAY_WIN.append(soup.find('span',{"class":"prediction-win-away"}).text.strip()) # AWAY_WIN

pd.DataFrame(
    {
        'Date': DATE,
        'HOME': HOME,
        'AWAY': AWAY,
        'HOME_GOAL':HOME_GOAL,
        'AWAY_GOAL':AWAY_GOAL,
        'HOME_WIN':HOME_WIN,
        'DRAW_WIN':DRAW_WIN,
        'AWAY_WIN':AWAY_WIN
    }
)
