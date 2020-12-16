from selectorlib import Extractor
import urllib.parse
from bs4 import BeautifulSoup
import requests

f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/database.txt","r")
data = f.readlines()

e = Extractor.from_yaml_file('C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/Amazon_selector.yml')
headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
rom = [', 8GB',', 16GB',', 32GB',', 64GB',', 128GB',', 256GB',', 512GB',', 1024GB',', 2048GB']
ROM = ['8GB','16GB','32GB','64GB','128GB','256GB','512GB','1024GB','2048GB']

s = ""
f1 = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/images.txt","a")
cnt = 0

for row in data:
    row = row.split('|||')
    if(row[0]=="Realme"):
        url = 'http://amazon.in/s?k=' + '+'.join(row[1].split())
        # print(url)
        r = requests.get(url,headers=headers)       
        data1 = e.extract(r.text)
        
        while data1['result'] is None : 
            r = requests.get(url,headers=headers)       
            data1 = e.extract(r.text)
        
        temp = data1['result']
        # print(temp)
        found = False
        for mobile in temp:
            if '(' in mobile['name']:
                name = mobile['name'][:mobile['name'].index('(')]
                if name[:-1] == row[1] or 'New '+row[1] == name[:-1]:
                    print(name,"Yes")
                    if row[0] != 'Apple':
                        for gb in rom:
                            if gb+" Storage" in mobile['name'] or gb in mobile['name']:
                                # f1.write(str(row[1]+'---'+mobile['img_url'][0])+"\n")
                                s += row[1]+'---'+mobile['img_url'][0] +'\n'
                                print(row[1]+'---'+mobile['img_url'][0])
                                found = True
                                break
                    else:
                        for gb in ROM:
                            if gb in mobile['name']:
                                # f1.write(str(row[1]+'---'+mobile['img_url'][0])+"\n")
                                s += row[1]+'---'+mobile['img_url'][0] +'\n'
                                print(row[1]+'---'+mobile['img_url'][0])
                                found = True
                                break
                if found :
                    break
        if not found :
            s += row[1]+'---'+'Not Found'+'\n'
            print(row[1]+'---'+'Not Found')
            # f1.write(row[1]+'---'+'Not Found'+'\n')
        # break