from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getGreen(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        nameList = bsObj.findAll("span", {"class":"green"})
        for name in nameList:
            print(name.get_text())
    except AttributeError as e:
        return None


green = getGreen("http://www.pythonscraping.com/pages/warandpeace.html")
if green == None:
    print("Green could not be found")
else:
    print(green)