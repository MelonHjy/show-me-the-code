import requests
from bs4 import BeautifulSoup


def findLink(url):
    r = requests.get(url)
    b = BeautifulSoup(r.content, 'html.parser')
    links = b.find_all('a')
    for link in links:
        print(link['href'])




findLink('https://www.baidu.com/')