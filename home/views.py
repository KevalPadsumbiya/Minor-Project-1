from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
import urllib.parse
from selectorlib import Extractor
from website import settings
from .models import mobileSpecsLink,UserData,Compare,Favourite,Comments,Votes
from bs4 import BeautifulSoup,SoupStrainer
import requests
from urllib.parse import unquote
from json import dumps
from .forms import regi_succe
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import string
import random
from django.core.mail import send_mail
import threading

# def index(request):
#     if request.method == 'POST':    # if searched something via search bar
#         return render(request,"home/index.html",{'searched':True,'search_text':request.POST['search_text']})
#     else:
#         return render(request,"home/index.html",{'searched' :False})

# def Test(request):
#     return render(request,"home/test.html",)

@csrf_exempt
def index(request):
    fhandle = open('items.txt')
    text = fhandle.read()
    fhandle.close()
    l = text.split(',')
    d = dict()
    d["data"] = l
    if request.method == 'POST':
        if request.session.get('user_name',0)!=0 and 'search_text' in request.POST:
            return render(request, "home/index.html",{'searched': True, 'search_text': request.POST['search_text'], 'list': dumps(d),'login_flag':True,'user_name':request.session['user_name']})
        elif request.session.get('user_name',0)!=0:
            return render(request,"home/index.html",{'login_flag':True,'user_name':request.session['user_name'],'searched':False,'list':dumps(d)})
        elif 'search_text' in request.POST:
            return render(request, "home/index.html",{'login_flag': False,'searched': True,'search_text': request.POST['search_text'],'list': dumps(d)})
        else:
            return render(request,"home/index.html",{'login_flag':False,'searched':False,'list':dumps(d)})
    else:
        if request.session.get('user_name',0)!=0:
            return render(request, "home/index.html", {'searched': False, 'list': dumps(d),'login_flag':True,'user_name':request.session['user_name']})
        else:
            return render(request,"home/index.html",{'searched' :False,'list':dumps(d),'login_flag':False})


def byBrand(request):
    fhandle = open('items.txt')
    text = fhandle.read()
    fhandle.close()
    li = text.split(',')
    d = dict()
    d["data"] = li
    l = ['Samsung','Apple','Oneplus','OPPO','Vivo','Asus','MI','Tecno','POCO','Realme']
    if 'search_text' in request.POST:
        queryset = list(mobileSpecsLink.objects.filter(mobile_name__startswith=request.POST.get('search_text')))
        text = request.POST.get('search_text')
    elif request.GET.get('brand') in l:
        queryset = list(mobileSpecsLink.objects.filter(brand_name=request.GET.get('brand')))
        text = request.GET.get('brand')
    names = []
    links = []
    p_key = []
    result = []
    fav_status = []
    compare_status = []
    for item in queryset:
        # print(item.pk)
        if len(Compare.objects.filter(mobile = get_object_or_404(mobileSpecsLink, pk = item.pk))):
            compare_status.append("Remove from compare")
        else:
            compare_status.append("Add to Compare")
        if len(Favourite.objects.filter(mobile = get_object_or_404(mobileSpecsLink, pk = item.pk))):
            fav_status.append("Remove from favourites")
        else:
            fav_status.append("Add to Favourites")
        p_key.append(item.pk)
        item = str(item)
        item = item.split('---')
        names.append(item[1])
        links.append(item[3])
        # for (a, b, c) in zip(names, links, p_key): 
        #     result.append([a,b,c])
        # print(result)
    result = zip(names,links,p_key,compare_status,fav_status)

    if request.session.get('user_name',0)!=0:
        return render(request, "home/display.html",
                          {'searched': True, 'search_text': text, 'result': result,
                           'size': len(names), 'list': dumps(d), 'login_flag':True,'user_name':request.session['user_name']})
    else:
        return render(request,"home/display.html",{'searched' :True,'search_text':text,'result':result,'size':len(names),'list':dumps(d)})


# def byBrand(request):
#     l = ['Samsung','Apple','Oneplus','OPPO','Vivo','Asus','MI','Tecno','POCO','Realme']
#     if request.GET.get('brand') in l:
#         queryset = list(mobileSpecsLink.objects.filter(brand_name=request.GET.get('brand')))
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

def price_scraper(url):
    r = requests.get(url)
    product = SoupStrainer('div',{'class':'_25b18c'})
    soup = BeautifulSoup(r.text,'html.parser',parse_only=product)
    return soup.div.div.contents[0]

def model(request):


    # print(request.GET.get('model'))
    l = []
    # result = []
    # print(request.GET.get('model'))
    model = request.GET.get('model')
    queryset = str(mobileSpecsLink.objects.get(pk=model))
    l = queryset.split('---')[2]
    # result.append(queryset.split('---')[1])
    # result.append(l.split(','))
    # result.append(queryset.split('---')[3])
    # result = zip(queryset.split('---')[1],l.split(','),queryset.split('---')[3])

    data = Comments.objects.filter(mobile = get_object_or_404(mobileSpecsLink, pk = model))
    names = []
    dates = []
    comment_text = []
    p_key = []
    vote_count = []
    up_voted = []
    down_voted = []
    delete_right = []

    for row in data:
        # print(row.pk)
        p_key.append(row.pk)
        temp = str(row).split('---')
        print(temp)
        names.append(temp[-3])
        dates.append(temp[-1])
        comment_text.append(temp[-2].split("||||"))
        if int(temp[-4]) == 0:
            vote_count.append(0)
        elif int(temp[-4]) < 0:
            vote_count.append(temp[-4])
        else:
            vote_count.append('+'+temp[-4])

        # print(temp[2])
        if request.session.get('user_name', 0) != 0:
            if(temp[-3]==request.session.get('user_name', 0)):
                delete_right.append(1)
            else:
                delete_right.append(0)
            OB = Votes.objects.filter(username = get_object_or_404(UserData, user_name = request.session['user_name']),comment=get_object_or_404(Comments, pk = row.pk))
            if len(OB) :
                # there will be always one row is he/she has already votes
                for tuple in OB :
                    temp1 = str(tuple).split('---')
                    if temp1[-2] == '1' :
                        up_voted.append(1)
                        down_voted.append(0)
                    else:
                        down_voted.append(1)
                        up_voted.append(0)
            else:
                up_voted.append(0)
                down_voted.append(0)
        else:
            up_voted.append(0)
            down_voted.append(0)
            delete_right.append(0)
    
    # print(names)
    
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

    mobile_name = queryset.split('---')[1][:-1]
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
    for name,pr,st,link in zip(varient,price,status,flipkart_url):
        print(name+" - "+pr+' - '+st+' - '+link)
    
    result1 = zip(varient,price,status,flipkart_url)
    # result.append([temp[-3],temp[-1],temp[-2].split("||||")])
    # print(up_voted)
    # print(down_voted)
    result = zip(names,dates,comment_text,p_key,vote_count,up_voted,down_voted,delete_right)
    if request.session.get('user_name', 0) != 0:
        return render(request,"home/view.html",{'Flipkart_result':result1,'count':len(names),'result':result,'pk':model,'login_flag':True,'user_name':request.session['user_name'],'name':queryset.split('---')[1],'image_url':queryset.split('---')[3],'spec':l.split(',')})
    else:
        return render(request,"home/view.html",{'Flipkart_result':result1,'count':len(names),'result':result,'pk':model,'name':queryset.split('---')[1],'image_url':queryset.split('---')[3],'spec':l.split(',')})

def signin(request):
    if request.session.get('user_name',0) == 0 :
        return render(request,"home/login.html")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def signup(request):
    if request.session.get('user_name',0) == 0 :
        return render(request,"home/register.html")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def compare(request):
    if request.session.get('user_name',0) == 0 :
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    # ids = request.GET.get('ids').split('-')
    data = Compare.objects.filter(username = get_object_or_404(UserData, user_name = request.session['user_name']))
    result = []
    name = []
    spec = []
    image_link = []
    p_key = []
    for row in data:
        # p_key.append(row.pk)
        model = str(row.mobile).split('---')
        temp = mobileSpecsLink.objects.filter(mobile_name = model[1])
        for el in temp:
            p_key.append(el.pk)
            break
        # print(str(row.mobile).split('---'))
        name.append(model[1])
        image_link.append(model[3])
        spec.append(model[2].split(','))
        # print()
    
    # print(data)
    # for id in ids:
    #     temp = []
    #     queryset = str(mobileSpecsLink.objects.get(pk=id))
    #     name.append(queryset.split('---')[1])
    #     l = queryset.split('---')[2]
    #     image_link.append(queryset.split('---')[3])
    #     spec.append(l.split(','))
    #     # print(queryset.split('---')[1])
    result = zip(name,spec,image_link,p_key)
    if request.session.get('user_name', 0) != 0:
        return render(request, "home/compare.html", {'size':len(name),'result': result,'login_flag':True,'user_name':request.session['user_name']})
    else:
        return render(request, "home/compare.html", {'result': result})




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

def news(request):
    url = 'https://news.google.com/search?gl=IN&pz=1&cf=all&hl=en-IN&q=topic:smartphones&ceid=IN:en'
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')

    desc = []
    by = []
    news_url = []
    image_url = []
    cnt = 0

    for news in soup.find_all('article', class_="MQsxIb"):
        temp = news.find('a', class_="DY5T1d")
        desc.append(temp.text)
        news_url.append('https://news.google.com/' + temp.attrs.get("href")[2:])
        by.append(news.find('a', class_="wEwyrc").text)
        cnt += 1
        if cnt == 25:
            break

    for news_by in soup.find_all('img', class_="tvs3Id"):
        image_url.append(news_by.attrs.get("src"))
        cnt -= 1
        if cnt == 0:
            break

    result = zip(desc, news_url, by, image_url)
    if request.session.get('user_name', 0) != 0:
        return render(request, "home/news.html", {'result': result,'login_flag':True,'user_name':request.session['user_name']})
    else:
        return render(request, "home/news.html", {'result': result})


@csrf_exempt
def validate_register(request):
    if request.is_ajax and request.method == 'POST':
        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_pass = request.POST.get("user_pass")
        name_count = UserData.objects.filter(user_name = user_name)
        email_count = UserData.objects.filter(user_email = user_email)
        if len(name_count)>0 and len(email_count)>0:
            return JsonResponse({"name": "yes", "email" : "yes"},status=200)
        elif len(name_count)>0:
            return JsonResponse({"name": "yes", "email" : "no"}, status=200)
        elif len(email_count)>0:
            return JsonResponse({"name":"no", "email": "yes"}, status=200)
        elif len(name_count)==0 and len(email_count)==0:
            userdata = UserData(user_name = user_name,user_email = user_email,password = user_pass)
            userdata.save()
            return JsonResponse({"name":"no", "email": "no"}, status=200)
    return JsonResponse({"error":""}, status=400)

@csrf_exempt
def validate_login(request):
    if request.is_ajax() and request.method=='POST':
        user_name = request.POST['username']
        user_pass = request.POST['pass']
        user_count = UserData.objects.filter(user_name = user_name).filter(password = user_pass)
        if len(user_count)==1:
            request.session['user_name'] = user_name
            return JsonResponse({'flag':"yes",'name':user_name},status=200)
        else:
            return JsonResponse({'flag':"no"},status=200)
    return JsonResponse({'error':""},status=400)

def logout(request):
    if request.session.get('user_name',0) == 0 :
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    try:
        del request.session['user_name']
    except KeyError:
        pass
    return render(request, "home/logout.html")

@csrf_exempt
def addToCompare(request):

    if request.is_ajax() and request.method=='POST':
        
        pri_key = request.POST['pri_key']
        # print(pri_key)
        
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        model_object = get_object_or_404(mobileSpecsLink, pk = pri_key)
        
        if len(Compare.objects.filter(mobile = model_object)):
            Compare.objects.filter(mobile = model_object).delete()
            # print("Deletde")
            return JsonResponse({'flag':"no",'cur': Compare.objects.count()},status=200)
        elif len(Compare.objects.all()) == 4:
            return JsonResponse({'flag':"full",'cur': Compare.objects.count()},status=200)
        else:
            # print("Added")
            r = Compare(username = user_object,mobile = model_object)
            r.save()
            return JsonResponse({'flag':"yes",'cur': Compare.objects.count()},status=200)


@csrf_exempt
def addToFavourite(request):

    if request.is_ajax() and request.method=='POST':
        # print("YESS")
        pri_key = request.POST['pri_key']
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        model_object = get_object_or_404(mobileSpecsLink, pk = pri_key)
        
        if len(Favourite.objects.filter(mobile = model_object)):
            Favourite.objects.filter(mobile = model_object).delete()
            return JsonResponse({'flag':"no"},status=200)
        else:
            r = Favourite(username = user_object,mobile = model_object)
            r.save()
            return JsonResponse({'flag':"yes"},status=200)


def favourite(request):
    if request.session.get('user_name',0) == 0 :
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

    data = Favourite.objects.filter(username = get_object_or_404(UserData, user_name = request.session['user_name']))
    result = []
    name = []
    spec = []
    image_link = []
    p_key = []
    for row in data:
        # p_key.append(row.pk)
        model = str(row.mobile).split('---')
        temp = mobileSpecsLink.objects.filter(mobile_name = model[1])
        for el in temp:
            p_key.append(el.pk)
            break
        # print(str(row.mobile).split('---'))
        name.append(model[1])
        image_link.append(model[3])
        # spec.append(model[2].split(','))
    result = zip(name,image_link,p_key)
    if request.session.get('user_name', 0) != 0:
        return render(request, "home/favourite.html", {'size':len(name),'result': result,'login_flag':True,'user_name':request.session['user_name']})
    else:
        return render(request, "home/favourite.html", {'result': result})

@csrf_exempt
def postComment(request):
    if request.is_ajax() and request.method=='POST':
        # print("Came")
        model_key = request.POST['model_key']
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        model_object = get_object_or_404(mobileSpecsLink, pk = model_key)
        
        l = request.POST['comment'].strip().split()
        fp = open('C:/Users/Lenovo/Desktop/New Website/website/offensivewordslist.txt','r')
        offensive_words = fp.readline().split(',')
        for word in l:
            for b_word in offensive_words:
                if word == b_word :
                    return JsonResponse({'flag':"bad"},status=200)
        # print(l,)             
        comment_text = list(request.POST['comment'].strip().split('\n'))
        # print(model_key,comment_text)
        comment_text = '||||'.join(comment_text)
        date = datetime.date.today()
        # print(model_key,date)
        # print(comment_text)
        if len(comment_text) == 0: 
            return JsonResponse({'flag':"no"},status=200)
        else:
            r = Comments(username = user_object,mobile = model_object,comment=comment_text,date=datetime.date.today(),vote_count=0)
            r.save()
            return JsonResponse({'flag':"yes",'updated_count':len(Comments.objects.all())},status=200)


@csrf_exempt
def upvoteComment(request):
    if request.is_ajax() and request.method=='POST':
        if request.session.get('user_name', 0) == 0:
            return JsonResponse({'flag':"not_logged_in"},status=200)

        model_key = request.POST['model_key']
        comment_key = request.POST['comment_key']
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        comment_object = get_object_or_404(Comments, pk = comment_key)
        model_object = get_object_or_404(mobileSpecsLink, pk = model_key)
        
        OB = Votes.objects.filter(comment=comment_object,username=user_object)
        if len(OB) :
            return JsonResponse({'flag':"already_voted"},status=200)
        
        # print(model_key,comment_key)

        r = Votes(username = user_object,mobile = model_object,comment=comment_object,upvote=1,downvote=0)
        r.save()
        ob = Comments.objects.get(pk=comment_key)
        ob.vote_count = ob.vote_count + 1
        ob.save()
        temp = ''
        if ob.vote_count == 0 :
            temp = 0
        elif ob.vote_count < 0 :
            temp = str(ob.vote_count)
        else :
            temp = '+'+str(ob.vote_count)
        return JsonResponse({'flag':"yes",'updated_count':temp},status=200)

@csrf_exempt
def downvoteComment(request):
    if request.is_ajax() and request.method=='POST':
        if request.session.get('user_name', 0) == 0:
            return JsonResponse({'flag':"not_logged_in"},status=200)

        model_key = request.POST['model_key']
        comment_key = request.POST['comment_key']
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        comment_object = get_object_or_404(Comments, pk = comment_key)
        model_object = get_object_or_404(mobileSpecsLink, pk = model_key)
        
        OB = Votes.objects.filter(comment=comment_object,username=user_object)
        if len(OB) :
            return JsonResponse({'flag':"already_voted"},status=200)

        # print(model_key,comment_key)
        
        r = Votes(username = user_object,mobile = model_object,comment=comment_object,upvote=0,downvote=1)
        r.save()
        ob = Comments.objects.get(pk=comment_key)
        ob.vote_count = ob.vote_count - 1
        ob.save()
        temp = ''
        if ob.vote_count == 0 :
            temp = 0
        elif ob.vote_count < 0 :
            temp = str(ob.vote_count)
        else :
            temp = '+'+str(ob.vote_count)
        return JsonResponse({'flag':"yes",'updated_count':temp},status=200)

@csrf_exempt
def Test(request):
    if request.is_ajax() and request.method=='POST':
        print("Came"+request.POST['comment_key'])
        comment_key = request.POST['comment_key']
        Comments.objects.filter(pk=comment_key).delete()
        return JsonResponse({'flag':"yes",'updated_count':len(Comments.objects.all())},status=200)

@csrf_exempt
def removeFromCompare(request):
    if request.is_ajax() and request.method=='POST':
        print("came")
        model_key = request.POST['model_key']
        print(model_key)
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        mobile_object = get_object_or_404(mobileSpecsLink, pk = model_key)
        Compare.objects.filter(mobile = mobile_object,username = user_object).delete()
        return JsonResponse({'flag':"yes",'model_key':model_key},status=200)

@csrf_exempt
def removeFromFavourites(request):
    if request.is_ajax() and request.method=='POST':
        print("came")
        model_key = request.POST['model_key']
        print(model_key)
        user_object = get_object_or_404(UserData, user_name = request.session['user_name'])
        mobile_object = get_object_or_404(mobileSpecsLink, pk = model_key)
        Favourite.objects.filter(mobile = mobile_object,username = user_object).delete()
        return JsonResponse({'flag':"yes",'model_key':model_key},status=200)

def forgot(request):
    if request.session.get('user_name',0) != 0 :
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
    return render(request,'home/forgot.html')

@csrf_exempt
def forgot_validate(request):
    if request.is_ajax() and request.method=="POST":
        mail = request.POST['mail']
        count = UserData.objects.filter(user_email=mail)
        if len(count)==1:
            try:
                t1 = threading.Thread(target=SendMail, args=(request.POST['mail'],))
                t1.start()
                # threading.thread.start_new_thread(SendMail,(request.POST['mail']))
                return JsonResponse({'flag':"yes"},status=200)
            except:
                print('no')
        else:
            return JsonResponse({'flag':"no"},status=200)
    return JsonResponse({'error':""},status=400)

def SendMail(mail):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    send_mail('from help center:', 'your password is : ' + str(res) + '. please keep this for login.',
              settings.EMAIL_HOST_USER, [mail], fail_silently=False)
    user = UserData.objects.get(user_email=mail)
    user.password = res
    user.save()