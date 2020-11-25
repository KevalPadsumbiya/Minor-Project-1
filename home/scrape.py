from selectorlib import Extractor
import requests
import urllib.parse
from bs4 import BeautifulSoup, SoupStrainer

def price_final(mobile_name):
    # print('%20'.join(item.split()))
    url = "http://flipkart.com/search?q="+'%20'.join(mobile_name.split())
    print(url)
    data = requests.get(url).text
    soup = BeautifulSoup(data,'lxml')

    rom = [', 8 GB',', 16 GB',', 32 GB',', 64 GB',', 128 GB',', 256 GB',', 512 GB',', 1024 GB',', 2048 GB']
    varient = []
    price = []
    flipkart_url = []
    status = []
    for item in soup.find_all('a',class_="_1fQZEK"):
        name = item.find('div',class_="_4rR01T").text
        temp = name
        if '(' in name:
            name = name[:name.index('(')]
            if name[:-1] == mobile_name:
                for gb in rom:
                    if gb in temp:
                        rs = item.find('div',class_="_30jeq3").text
                        current_status = "available"
                        try :
                            current_status = item.find('div',class_="_3G6awp").text
                        except :
                            pass
                        varient.append(temp[temp.index('('):])
                        price.append(rs[1:])
                        status.append(current_status)
                        flipkart_url.append("https://www.flipkart.com"+item['href'])
                        # print(temp,gb,rs[1:],status,"https://www.flipkart.com"+item['href'])
                        break
    for name,price,status,link in zip(varient,price,status,flipkart_url):
        print(name+" - "+price+' - '+status+' - '+link)
price_final('Samsung Galaxy A30')