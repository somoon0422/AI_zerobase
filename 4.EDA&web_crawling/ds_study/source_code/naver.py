# 4개데이터 수집
import pandas as pd
import requests
#from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"
response = requests.get(url) 
# resuqests.get()
# requests.post()
#  url을 통해서 서버에 요청
#response # 200 : 정상 (HTTP상태코드)
soup = BeautifulSoup(response.text, 'html.parser')

#class 면 .을 사용 하고, id 면 #을 사용

exchangeList = soup.select("#exchangeList > li") 
len(exchangeList) , exchangeList[0]


exchange_datas = []
baseurl = "https://finance.naver.com"

for item in exchangeList:
    data = {
        "title" : item.select_one(".h_lst").text,
        "exchange" : item.select_one(".value").text,
        "change" : item.select_one(".change").text,
        "updown" : item.select_one("div.head_info.point_dn > .blind").text,
        "link" : baseurl + item.select_one('a').get('href')
    } 
    
    exchange_datas.append(data)
    
df = pd.DataFrame(exchange_datas)
df.to_excel("naverfinance.xlsx", index=False)