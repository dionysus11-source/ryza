
import requests
from bs4 import BeautifulSoup

def searchKeyword(keyword):
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    url = 'https://bbs.ruliweb.com/game/85195/read/9418448'
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.content,'lxml')
    # keyword = '깨끗한 물'
    ret = keyword + '\n'
    divs = bs.select('tr')
    cnt = 1
    for div in divs:
        tds = div.select('td')
        if len(tds) == 3:
            items = tds[0]
            locations = tds[1]
            descs = tds[2]
            if keyword in items.text:
                ret += str(cnt) + ') '+ items.text + ': 장소:'  +  locations.text + '\n특징: ' + descs.text + '\n'
                cnt += 1
    if cnt == 1:
        return 'Not found'
    else:
        return ret
