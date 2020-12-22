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








# param = dict()
    # param['q'] = queryset.split('---')[1]
    # url = "http://flipkart.com/search?"+urllib.parse.urlencode(param)
    # e = Extractor.from_yaml_file('C:/Users/Lenovo/Desktop/Minor-Project-I-master/home/selector.yml')
    # r = requests.get(url)
    # data = e.extract(r.text)
    # j=0
    # color=list()
    # variant=dict()
    # price_variant=dict()
    # Links = []
    # for links in data['products']:
    #     color.clear()
    #     variant.clear()
    #     price_variant.clear()
    #     url = 'http://flipkart.com'+links['url']
    #     r = requests.get(url)
    #     product = SoupStrainer('div',{'class':'_3wmLAA'})
    #     soup = BeautifulSoup(r.text,'html.parser',parse_only=product)
    #     if len(soup)==1:
    #         i=0
    #         for s in soup.div.children:
    #             i=i+1
    #         if i>1:
    #             for s in soup.div.children:
    #                 for d in s.div.ul.children:
    #                     if s.div.span.string == 'Color':
    #                         for q in d.children:
    #                             if q.div['class'] == ['_3Oikkn', '_3_ezix', '_2KarXJ']:
    #                                 color.append(q.div.contents[0])
    #                     else:
    #                         price = price_scraper('http://flipkart.com'+d.a['href'])
    #                         # print(d.a['href'])
    #                         print('http://flipkart.com'+d.a['href'])
    #                         # if 'http://flipkart.com'+d.a['href'] not in Links:
    #                         Links.append('http://flipkart.com'+d.a['href'])
    #                         # links.append('http://flipkart.com'+d.a['href'])
    #                         price_variant[d.div.div.contents[0]]=price
    #                         if variant.get(s.div.span.string,False):
    #                             variant[s.div.span.string].append(d.div.div.contents[0])
    #                         else:
    #                             variant[s.div.span.string]=list()
    #                             variant[s.div.span.string].append(d.div.div.contents[0])
    #             break
    #         else:
    #             j=j+1
    #             if j>10:
    #                 price_variant['one']=price_scraper('http://flipkart.com'+data['products'][0]['links'])
    #                 break
    #     else:
    #         j=j+1
    #         if j>10:
    #             price_variant['one']=price_scraper('http://flipkart.com'+data['products'][0]['links'])
    #             break
    # print(color)
    # print(variant)
    # print(price_variant)
    # print(Links)
    # result1 = []
    # l1 = [] # var
    # l2 = [] # price
    # l3 = [] # url
    # for var in variant['Storage']:
    #     print(price_variant[var])
    #     # result1.append([var,price_variant[var][1:]])
    #     l1.append(var)
    #     l2.append(price_variant[var][1:])
    # for el in l1:
    #     for url in Links:
    #         if el.split()[0]+'-gb' in url:
    #             l3.append(url)
    # # print(result1)
    # print(l1)
    # print(l2)
    # print(l3)
    # result1 = zip(l1,l2,l3)




# def byBrand(request):
#     l = ['Samsung','Apple','Oneplus','OPPO','Vivo','Asus','MI','Tecno','POCO','Realme']
#     if request.GET.get('brand') in l:
#         queryset = list(deviceDetails.objects.filter(brand_name=request.GET.get('brand')))
#         names = []
#         links = []
#         p_key = []
#         result = []
#         for item in queryset:
#             # print(item.pk)
#             p_key.append(item.pk)
#             item = str(item)
#             item = item.split('---')
#             names.append(item[1])
#             links.append(item[3])
#         # for (a, b, c) in zip(names, links, p_key): 
#         #     result.append([a,b,c])
#         # print(result)
#         result = zip(names,links,p_key)
#         return render(request,"home/display.html",{'searched' :True,'search_text':request.GET.get('brand'),'result':result,'size':len(names)})
#     else:
#         return render(request,"home/index.html",{'searched' :False})










# def news(request):

#     url = 'https://news.google.com/search?gl=IN&pz=1&cf=all&hl=en-IN&q=topic:smartphones&ceid=IN:en'
#     data = requests.get(url).text
#     soup = BeautifulSoup(data,'lxml')

#     desc = []
#     by = []
#     news_url = []
#     image_url = []
#     cnt = 0
    
#     for news in soup.find_all('article',class_="MQsxIb"):
#         temp = news.find('a',class_="DY5T1d")
#         desc.append(temp.text)
#         news_url.append('https://news.google.com/'+temp.attrs.get("href")[2:])
#         by.append(news.find('a',class_="wEwyrc").text)
#         cnt += 1
#         if cnt == 25:
#             break

#     for news_by in soup.find_all('img',class_="tvs3Id"):
#         image_url.append(news_by.attrs.get("src"))
#         cnt -= 1
#         if cnt == 0:
#             break

#     result = zip(desc,news_url,by,image_url)
    
#     return render(request,"home/news.html",{'result':result})







# {% load static %}

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="utf-8"/>
#     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#     <link rel="apple-touch-icon" sizes="76x76" href="../../static/img/apple-icon.png">
#     <link rel="icon" type="image/png" href="../../static/img/favicon.png">
#     <title>
#         {{title}}
#     </title>

#     <link rel="stylesheet" href="sweetalert2/dist/sweetalert2.min.css">

#     <!--     Fonts and icons     -->
#     <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700">
#     <link rel="stylesheet" type="text/css" href="https://use.fontawesome.com/releases/v5.0.6/css/all.css">
#     <!-- Nucleo Icons -->
#     <link rel="stylesheet" type="text/css" href="{% static '/css/nucleo-icons.css' %}"/>
#     <link rel="stylesheet" type="text/css" href="{% static '/css/nucleo-svg.css' %}"/>
#     <!-- Font Awesome Icons -->
#     <link rel="stylesheet" type="text/css" href="../../static/css/font-awesome.css "/>
#     <link rel="stylesheet" type="text/css" href="../../static/css/nucleo-svg.css "/>
#     <link rel="stylesheet" type="text/css" href="{% static '/css/font-awesome.css' %}"/>
#     <link rel="stylesheet" type="text/css" href="{% static '/css/nucleo-svg.css' %}"/>
#     <!-- CSS Files -->
#     <link rel="stylesheet" type="text/css" href="../../static/css/argon-design-system.css?v=1.2.0"/>
#     <link rel="stylesheet" type="text/css" href="{% static '/css/argon-design-system.css?v=1.2.0' %}"/>
#     <title>Profile</title>
#     <style>
#         table,th,td,tr{
#             border: 2px solid black;
#             border-collapse: collapse;
#             padding: 20px;
#         }
#     </style>
#         <script src="../../static/js/core/jquery.min.js" type="text/javascript"></script>
# <script src="../../static/js/core/popper.min.js" type="text/javascript"></script>
# <script src="../../static/js/core/bootstrap.min.js" type="text/javascript"></script>
# <script src="../../static/js/plugins/perfect-scrollbar.jquery.min.js"></script>
# <!--  Plugin for Switches, full documentation here: http://www.jque.re/plugins/version3/bootstrap.switch/ -->
# <script src="../assets/js/plugins/bootstrap-switch.js"></script>
# <!--  Plugin for the Sliders, full documentation here: http://refreshless.com/nouislider/ -->
# <script src="../../static/js/plugins/nouislider.min.js" type="text/javascript"></script>
# <script src="../../static/js/plugins/moment.min.js"></script>
# <script src="../../static/js/plugins/datetimepicker.js" type="text/javascript"></script>
# <script src="../../static/js/plugins/bootstrap-datepicker.min.js"></script>
# <!-- Control Center for Argon UI Kit: parallax effects, scripts for the example pages etc -->
# <!--  Google Maps Plugin    -->
# <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_KEY_HERE"></script>
# <script src="../../static/js/argon-design-system.min.js?v=1.2.0" type="text/javascript"></script>
# <script src="https://cdn.trackjs.com/agent/v3/latest/t.js"></script>

# <!-- Sweet Alert 2 -->
# <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
# <script src="sweetalert2/dist/sweetalert2.all.min.js"></script>
# <!-- Include a polyfill for ES6 Promises (optional) for IE11 -->
# <script src="https://cdn.jsdelivr.net/npm/promise-polyfill@8/dist/polyfill.js"></script>
# <script src="sweetalert2/dist/sweetalert2.min.js"></script>


# <script>

#         function delete_com(comment_key,model_key){
#                $.ajax({
#                         type:'POST',
#                         url:'{% url 'test' %}',
#                         data:{
#                             model_key:model_key,
#                             comment_key:comment_key,
#                         },
#                         success:function(response)
#                         {

#                             var flag = response['flag'];
#                             if(flag == 'no')
#                             {
#                                 alert("There is some error");
#                             }
#                             else if(flag == 'yes')
#                             {
#                                 Swal.fire({
#                                     icon: 'success',
#                                     title: 'Comment has successfully deleted !',
#                                     showConfirmButton: false,
#                                     timer: 2000
#                                   });
#                                 location.reload();
#                             }
#                         },
#                         error:function(response){
#                             alert(response["responseJSON"]["error"]);
#                         }
#                     });
#         }
#     </script>
#     <style>
#         body
#         {
#         }
#         table,tr,td
#         {

#         }
#     </style>
# </head>
# <body>
#         <center>
#             <h2>Your Comments</h2>
#             <br>
#             <table>
#             <tr>
#                 <!-- <th>pk_m</th>
#                 <th>pk_c</th> -->
#                 <th>Name</th>
#                 <th>Date</th>
#                 <th>Comment</th>
#                 <th>Action</th>
#             </tr>
#                 {% for pk_m,pk_c,mobile_name,date,comment_text in result %}
#                     <tr>
#                     <!-- <td>{{ pk_m }}</td> -->
#                         <!-- <td>{{ pk_c }}</td> -->
#                     <td><a href="/view?model={{  pk_m }}">{{ mobile_name }}</a> </td>
#                     <td>{{ date }}</td>
#                     <td>{{ comment_text }}</td>
#                         {% csrf_token %}
#                     <td><button class="btn" style="background: red; color:white;" onclick="delete_com({{pk_c}},{{pk_m}})">delete</button></td>
#                     </tr>
#                 {% endfor %}
#             </table>
#         </center>
# </body>
# </html>