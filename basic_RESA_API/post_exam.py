import requests

jsonInfo = { 'name': 'kim', 'job': 'kakao', 'array': {'one':'1,2', 'two':'3,4'} }

r = requests.post("https://httpbin.org/post", data=jsonInfo)
print(r.text)