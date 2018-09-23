import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

titleList = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')

for idx, title in enumerate(titleList, 1):
    print("{}{} {}".format(idx, '위', title.text))