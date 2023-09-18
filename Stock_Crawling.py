import requests
from bs4 import BeautifulSoup


# 일별 시세 두번째 페이지 크롤링
res2 = requests.get('https://finance.naver.com/item/sise_day.naver?code=005930&page=2', headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
bs = BeautifulSoup(res2.text, 'html.parser')

for data in bs.select('table.type2 > tr')[4:]:
    if data.select_one('th') == None and len(data.select('td')) == 7:
        print(data.select('td')[0].text)
        print(data.select('td.num')[0].text)


# 일별 시세 세번째 페이지 크롤링
res3 = requests.get('https://finance.naver.com/item/sise_day.naver?code=005930&page=3', headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
bs = BeautifulSoup(res3.text, 'html.parser')

for data in bs.select('table.type2 > tr'):
    if data.select_one('th') == None and len(data.select('td')) == 7:
        print(data.select('td')[0].text)
        print(data.select('td.num')[0].text)


# 일별 시세 네번째 페이지 크롤링
res4 = requests.get('https://finance.naver.com/item/sise_day.naver?code=005930&page=4', headers={'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
bs = BeautifulSoup(res4.text, 'html.parser')

for data in bs.select('table.type2 > tr')[2:6]:
    if data.select_one('th') == None and len(data.select('td')) == 7:
        print(data.select('td')[0].text)
        print(data.select('td.num')[0].text)