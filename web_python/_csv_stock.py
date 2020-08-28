"""import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from gids import builder

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
url ='https://datalab.naver.com/keyword/realtimeList.naver?where=main'
res = requests.get(url, headers = headers)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('span.item_title')

i=1
for item in data:
    print(int(i), '위 : ',item.get_text())
    i=i+1"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
# 한글 검색 자동 변환
url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img', limit=10)

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open('사진' + plusUrl + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
print('다운로드 완료')