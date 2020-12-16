# from selectorlib import Extractor
# import urllib.parse
# from bs4 import BeautifulSoup
# import requests

# f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","r")
# data = f.readlines()

# e = Extractor.from_yaml_file('C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/Amazon_selector.yml')
# headers = {
#         'dnt': '1',
#         'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'navigate',
#         'sec-fetch-user': '?1',
#         'sec-fetch-dest': 'document',
#         'referer': 'https://www.amazon.com/',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#     }
# rom = [', 8GB',', 16GB',', 32GB',', 64GB',', 128GB',', 256GB',', 512GB',', 1024GB',', 2048GB']
# ROM = ['8GB','16GB','32GB','64GB','128GB','256GB','512GB','1024GB','2048GB']

# s = ""
# f1 = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/images.txt","a")
# cnt = 0
# page_nos = {'Apple':20}
# image_url = {}
# # for row in data:
# #     row = row.split('|||')
# #     if(row[0]=="Apple"):
# # prefix= 'https://www.amazon.in/s?i=electronics&bbn=1389432031&rh=n%3A976419031%2Cn%3A1389401031%2Cn%3A1389432031%2Cn%3A1805560031%2Cp_89%3A'
# # brand = 'Apple'
# # middle = '&s=popularity-rank&dc&page='
# # suffix = '&qid=1608103548&rnid=1389432031&ref=sr_pg_2'

# prefix = 'https://www.amazon.in/s?i=merchant-items&me=A14CZOWI0VEHLG&rh=p_4%3A'
# brand = 'Apple'
# middle = '&dc&page='
# suffix = '&marketplaceID=A21TJRUUN4KGV&qid=1608106049'
# # url = 'http://amazon.in/s?k=' + '+'.join(row[1].split())
# # print(url)
# for i in range(1,page_nos['Apple']+1):
#     url = prefix + brand + middle + str(i) + suffix
#     print(url)

#     r = requests.get(url,headers=headers)       
#     data1 = e.extract(r.text)
    
#     # print(data1)

#     while data1['result'] is None : 
#         r = requests.get(url,headers=headers)       
#         data1 = e.extract(r.text)
    
#     temp = data1['result']

#     for device in temp:
#        print(device['name'],device['img_url'])
#     temp = data1['result']

    
#     for row in data:
#         row = row.split('|||')
#         # print(row[1])
#         for device in temp:
#             if row[1] in device['name'] and row[1] not in image_url:
#                 image_url[row[1]] = device['img_url']

# for key,value in image_url.items():
#     print(key,value)


# # for row in data:
# #     row = row.split('|||')
# #     if(row[0]=="Realme"):
# #         url = 'http://amazon.in/s?k=' + '+'.join(row[1].split())
# #         # print(url)
# #         r = requests.get(url,headers=headers)       
# #         data1 = e.extract(r.text)
        
# #         while data1['result'] is None : 
# #             r = requests.get(url,headers=headers)       
# #             data1 = e.extract(r.text)
        
# #         temp = data1['result']
# #         # print(temp)
# #         found = False
# #         for mobile in temp:
# #             if '(' in mobile['name']:
# #                 name = mobile['name'][:mobile['name'].index('(')]
# #                 if name[:-1] == row[1] or 'New '+row[1] == name[:-1]:
# #                     print(name,"Yes")
# #                     if row[0] != 'Apple':
# #                         for gb in rom:
# #                             if gb+" Storage" in mobile['name'] or gb in mobile['name']:
# #                                 # f1.write(str(row[1]+'---'+mobile['img_url'][0])+"\n")
# #                                 s += row[1]+'---'+mobile['img_url'][0] +'\n'
# #                                 print(row[1]+'---'+mobile['img_url'][0])
# #                                 found = True
# #                                 break
# #                     else:
# #                         for gb in ROM:
# #                             if gb in mobile['name']:
# #                                 # f1.write(str(row[1]+'---'+mobile['img_url'][0])+"\n")
# #                                 s += row[1]+'---'+mobile['img_url'][0] +'\n'
# #                                 print(row[1]+'---'+mobile['img_url'][0])
# #                                 found = True

# #                                 break
# #                 if found :
# #                     break
# #         if not found :
# #             s += row[1]+'---'+'Not Found'+'\n'
# #             print(row[1]+'---'+'Not Found')
#             # f1.write(row[1]+'---'+'Not Found'+'\n')
#         # break

from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
from urllib.request import Request,urlopen
import re 

# url = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DVivo&otracker=nmenu_sub_Electronics_0_Vivo'
# req = Request(url)
# webpage=urlopen(req).read()


f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","w")


# brands = ['Nokia','LG','Mi','Realme','Samsung','OPPO','Apple','Asus','Vivo','Honor','POCO','Micromax','Motorola','Google','HTC','Sony','Huawei','Intex']
brands = ['Mi']
main_url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3D"

for brand in brands :
    url = main_url + brand + '&page='
    # print(url)
    data = requests.get(url).text
    soup = BeautifulSoup(data,'lxml')
    try :
        total_pages = int(soup.find('div',class_="_2MImiq").span.text.split()[-1])
        print(total_pages)
    except:
        total_pages = 1

    for page_no in range(1,total_pages+1):
        req = Request(url + str(page_no))
        webpage = urlopen(req).read()
        print(page_no)
        # print(url + str(page_no))
        soup = BeautifulSoup(webpage,'html.parser')
        html_obj = soup.prettify('utf-8')
        # print(str(html_obj))
        data = str(html_obj)
        f.write(data[data.find("\"media\""):])
        data = data[data.find("\"media\""):]
        # print(data)
        # print(data)
        # continue
        # print(url)
        # res = [i.start() for i in re.finditer("\"media\"", data)]

    f.close()
    f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","r")
    data = f.read()
    image_urls = dict()
    for i in re.finditer("\"media\"", data):
        # print(i.start())
        
        # fetching url
        url = ""
        name = ""
        j = i.start()
        while data[j:j+7] != "\"url\":\"" :
            j += 1
        j += 7
        while data[j] != "\"":
            url += data[j]
            j += 1

        url = url.replace('{@width}/{@height}','312/312')
        url = url.replace('?q={@quality}','')
        # print(url)

        # fetching name
        while data[j:j+8] != "\"titles\"":
            j += 1
        j += 8

        while data[j:j+9] != "\"title\":\"":
            j += 1
        j += 9
        # print("j :",j)
        while data[j+1] != "(":
            name += data[j]
            # print(data[j],end="")
            j += 1
        
        if name not in image_urls:
            image_urls[name] = url
        # print(name+' - '+url)
        # print()

    f.close()

    f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/image_url.txt","a")
    for name,url in image_urls.items():
        # print(name,url)
        f.write(name+'|||'+url+'\n')
    f.close() 