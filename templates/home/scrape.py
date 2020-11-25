from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

url = 'https://news.google.com/search?gl=IN&pz=1&cf=all&hl=en-IN&q=topic:smartphones&ceid=IN:en'
data = requests.get(url).text
soup = BeautifulSoup(data,'lxml')

for news in soup.find_all('article',class_="MQsxIb"):
    temp = news.find('a',class_="DY5T1d")
    print(temp.attrs.get("href")[2:]) 
    print(temp.text +'-'+'https://news.google.com/'+temp.attrs.get("href")[2:]+'-'+news.find('a',class_="wEwyrc").text)

for news_by in soup.find_all('img',class_="tvs3Id"):
    print(news_by.attrs.get("src"))