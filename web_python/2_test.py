import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list.nhn?titleId=20853"
res= requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

total_rates=0
cartoons=soup.find_all("div",attrs={"class":"rating_type"})

for cartoon in cartoons:
    rate=cartoon.find("strong").get_text()
    print(rate)
    total_rates+=float(rate)
print("전체점수 : ",total_rates)
print("평균 점수 : ",total_rates/len(cartoons))