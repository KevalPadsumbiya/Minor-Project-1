from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
from urllib.request import Request,urlopen
import re 

f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","w")

# brands = ['Mi','Realme','Samsung','OPPO','Apple','Asus','Vivo','Honor','POCO','Micromax','Motorola','Google','HTC','Sony','Huawei','Intex','Nokia','LG','Panasonic','Nubia]
brands = ['Nubia']
main_url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3D"

cnt = 0
for brand in brands :
    url = main_url + brand + '&page='
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
        soup = BeautifulSoup(webpage,'html.parser')
        html_obj = soup.prettify('utf-8')
        data = str(html_obj)
        f.write(data[data.find("\"media\""):])
        data = data[data.find("\"media\""):]

    f.close()
    f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","r")
    data = f.read()
    image_urls = dict()
    for i in re.finditer("\"media\"", data):      
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

        while data[j+1] != "(":
            name += data[j]
            j += 1
        
        if name not in image_urls and len(name)<100:
            image_urls[name] = url
            cnt += 1

    f.close()

    f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/image_url.txt","a")
    for name,url in image_urls.items():
        f.write(name+'|||'+url+'\n')
    f.close()

    print(cnt)