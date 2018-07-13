import requests
from bs4 import BeautifulSoup
import os
import re


def goodClawer(url, topath):
    headers ={
        'User-Agent': "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"
    }
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    all_img = soup.find_all('a', href=re.compile(r"http://image[\w./]+"))
    print(all_img)
    n = 1
    for img in all_img:
        img_path = img['href']
        data = requests.get(img_path).content
        path = os.path.join(topath, str(n+20)+'.jpg')
        with open(path, 'wb') as f:
            f.write(data)
        n += 1



url = r'http://www.1905.com/newgallery/hdpic/914524.shtml#1'
topath = os.path.join(os.getcwd(), 'bimage')
goodClawer(url, topath)
