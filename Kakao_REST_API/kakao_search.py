import requests
import json

API_HOST = 'https://dapi.kakao.com/'
headers = {'Content-Type': 'application/json; charset=utf-8',
           'Authorization': 'KakaoAK f20d837d1d730bb6e3e33f93c29e108c'}

def req(path, query, method, data={}):
    url = API_HOST + path
    print(url)
    print('HTTP Method: %s' % method)
    print('Request URL: %s' % url)
    print('Headers: %s' % headers)
    print('QueryString: %s' % query)

    if method == 'GET':
        return requests.get(url, query, headers=headers)
    else:
        return requests.post(url, headers=headers, data=data)

resp = req('/v2/search/image', 'query=설현', 'GET')

jsonObj = json.loads(resp.text)

print("response status:\n%d" % resp.status_code)
print("response headers:\n%s" % resp.headers)
#print("response body:\n%s" % resp.text)
print(jsonObj)