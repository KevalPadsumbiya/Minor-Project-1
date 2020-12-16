from bs4 import BeautifulSoup
import requests
from urllib.parse import unquote
from urllib.request import Request,urlopen

# # brands = ['Nokia','LG,'Mi','Realme','Samsung','OPPO','Apple','Asus','Vivo','Honor','POCO','Micromax','Motorola','Google','HTC','Sony','Huawei','Intex']
# brands = ['Apple']
# main_url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3D"

# # f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/database.txt","a")
# # f1 = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/items.txt","a")

# for brand in brands :
#     url = main_url+brand + '&page='
#     print(url)
#     data = requests.get(url).text
#     soup = BeautifulSoup(data,'lxml')
#     try :
#         total_pages = int(soup.find('div',class_="_2MImiq").span.text.split()[-1])
#         print(total_pages)
#     except:
#         total_pages = 1

#     cnt = 0
#     name_list = dict()
#     name_list1 = dict()
#     for i in range(1,total_pages+1):
#         data = requests.get(url+str(i)).text
#         soup = BeautifulSoup(data,'lxml')
#         for outer_box in soup.find_all('a',class_="_1fQZEK"):
#             name = outer_box.find('div',class_="_4rR01T").text
#             if '(' in name:
#                 name = name[:name.index('(')][:-1]
#                 specs = []
#                 # for specification in outer_box.find_all('li',class_="rgWa7D"):
#                     # print(specification.text)
#                     # specs.append(specification.text)
#                 # print(name.split()[0]+' - '+name+' - ','---'.join(specs))
#                 if name not in name_list:
#                     # print(name)
#                     try :
#                         # f.write(str(name.split()[0]+'|||'+name+'|||'+'---'.join(specs))+'\n')
                        
#                         cc = outer_box.find('img',class_="_396cs4")
#                         print(cc)
#                         # print(name.split()[0]+' - '+name+'-'+outer_box.find('div',class_="_30jeq3").text[1:]+outer_box.find('img',class_="_3exPp9"))
#                         cnt += 1
#                         # f1.write(name+' ,')
#                         # name_list1[name] = '---'.join(specs)
#                         name_list[name] = outer_box.find('div',class_="_30jeq3").text[1:]
#                     except :
#                         pass
#                 # elif outer_box.find('div',class_="_30jeq3").text[1:] < name_list[name]:
#                 #     print('Yes-'+name.split()[0]+' - '+name+'-'+outer_box.find('div',class_="_30jeq3").text[1:])
#                 #     name_list1[name] = '---'.join(specs)
#                 #     name_list[name] = outer_box.find('div',class_="_30jeq3").text[1:]
#     # for t1,t2 in zip(name_list.items(),name_list1.items()):
#     #     # print(t1[0],t1[1])
#     #     try :
#     #         f.write(str(brand+'|||'+t1[0]+'|||'+t1[1]+'|||'+t2[1])+'\n')
#     #         f1.write(t1[0]+' ,')
#     #     except:
#     #         pass
#     # for key,value in name_list1.items():
#     #     print(key,value)
#     print(cnt)

url = 'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi'
req = Request(url)
webpage=urlopen(req).read()
import re 

f = open("C:/Users/Lenovo/Desktop/Github Repo/MInot-Project-1/home/temp.txt","w")

soup = BeautifulSoup(webpage,'html.parser')
html_obj = soup.prettify('utf-8')
# print(str(html_obj))
data = str(html_obj)
f.write(data[data.find("\"media\""):])
data = data[data.find("\"media\""):]
# res = [i.start() for i in re.finditer("\"media\"", data)]
for i in re.finditer("\"titles\":{\"title\":\"", data):
    print(i.start())
    
    # data = data[i.start()+19:] 
    j = i.start()+19
    while data[j+2] != "(":
        print(data[j],end="")
        j += 1
    # print(data[i.start()+19:].find("("))
    # print(data[i.start()+19:data[i.start()+19:].find("(")])

# print(res)
# print(len(res))
# for outer_box in soup.find_all('img',class_="_396cs4"):
#     print(outer_box)