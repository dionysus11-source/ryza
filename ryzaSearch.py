import requests
from bs4 import BeautifulSoup
import os.path
import pandas as pd

filename = 'ryza.csv'
def downloadCsv():
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    url = 'https://bbs.ruliweb.com/game/85195/read/9418448'
    r = requests.get(url, headers=header)
    bs = BeautifulSoup(r.content,'lxml')
    divs = bs.select('#board_read > div > div.board_main > div.board_main_view > div.view_content.autolink > div > table > tbody > tr')
    item = []
    location = []
    info = []
    col = divs[0].text.split('\n')[1:4]
    col1, col2, col3 = tuple(col)
    del divs[0]
    for i in divs:
        a = i.text.split('\n')[1:4]
        item.append(a[0])
        location.append(a[1])
        info.append(a[2])
    data = {col1:item, col2:location, col3:info}
    df = pd.DataFrame(data)
    df.to_csv(filename)

#if not os.exist(filename):
def searchKeyword(keyword):
    if not os.path.exists(filename):
        downloadCsv()
    df = pd.read_csv(filename)
    cnt = 1
    ret = keyword + '\n'
    for i in df.index:
        target = df.at[i, '소재']
        if keyword in target:
            ret += str(cnt) + ') '+ target + ': 장소:'  +  df.at[i, '입수 장소'] + '\n특징: ' + df.at[i, '자세한 사항'] + '\n'
            cnt += 1
    if cnt == 1:
        return 'Not found'
    else:
        return ret
