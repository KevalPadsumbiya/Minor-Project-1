from selectorlib import Extractor
import urllib.parse
from bs4 import BeautifulSoup
import requests

f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","r")
data = f.readlines()

e = Extractor.from_yaml_file('C:/Users/Lenovo/Desktop/Last-MP1/Minor-Project-1/home/Amazon_selector.yml')
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

prefix = 'https://www.amazon.in/s?k='
device_name = input()
suffix = '&rh=n%3A1805560031&ref=nb_sb_noss'

url = prefix + '+'.join(device_name.split()) + suffix

print(url)

r = requests.get(url,headers=headers)       
data1 = e.extract(r.text)

# print(data1)

while data1['result'] is None : 
    r = requests.get(url,headers=headers)       
    data1 = e.extract(r.text)

temp = data1['result']

# print(temp)

for device in temp:
    try:
        if device_name in device['name'] and 'Case' not in device['name'] and 'case' not in device['name']:
            print(device['name']+' - '+device['price'][1:]+' - https://amazon.in'+device['url']+' - '+ device['rating']+' - '+ device['total_ratings'])
    except:
        pass