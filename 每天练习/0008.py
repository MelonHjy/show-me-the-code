import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.baidu.com/')
b = BeautifulSoup(r.content, 'html.parser')
print(b.body.text)