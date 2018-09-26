import json
import urllib.request

urlTicker = urllib.request.urlopen('https://api.androidhive.info/contacts/')
readTicker = urlTicker.read()

dict = json.loads(readTicker)
dict2 = json.loads(readTicker)

for h in dict['contacts']:
    print(h['id'])

for h in dict2['contacts']:
    print(h['id'], h['phone']['mobile'])