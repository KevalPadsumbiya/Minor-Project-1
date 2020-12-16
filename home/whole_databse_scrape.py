from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote

# brands = ['Mi','Realme','Samsung','OPPO','Apple','Asus','Vivo','Honor','POCO','Micromax','Motorola','Google','HTC','Sony','Huawei','Intex']
brands = ['Intex']
url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3D"

f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/database.txt","a")
for brand in brands :
    url += brand + '&page='
    data = requests.get(url).text
    soup = BeautifulSoup(data,'lxml')
    total_pages = int(soup.find('div',class_="_2MImiq").span.text.split()[-1])
    print(total_pages)

    cnt = 0
    name_list = dict()
    for i in range(1,total_pages+1):
        data = requests.get(url+str(i)).text
        soup = BeautifulSoup(data,'lxml')
        for outer_box in soup.find_all('a',class_="_1fQZEK"):
            name = outer_box.find('div',class_="_4rR01T").text
            if '(' in name:
                name = name[:name.index('(')][:-1]
                specs = []
                for specification in outer_box.find_all('li',class_="rgWa7D"):
                    # print(specification.text)
                    specs.append(specification.text)
                # print(name.split()[0]+' - '+name+' - ','---'.join(specs))
                if name not in name_list :
                    try :
                        f.write(str(name.split()[0]+'|||'+name+'|||'+'---'.join(specs))+'\n')
                        print(name.split()[0]+' - '+name)
                        cnt += 1
                    except :
                        pass
                name_list[name] = 1
    print(cnt)


