from django.shortcuts import render, redirect
from .models import Titles, Towatch, Watched, Liked, Cache
from .imdbscrapper import imdb
from .rtscrapper import rt
from .mcscraper import mc
import time

# Create your views here.

#To remove titles from your lists (from lists page)
def rm_list(request, arg):
    if not request.user.is_authenticated:
        return redirect('welcome')
    if arg[:2]=='tw':
        mem=Towatch.objects.get(user=request.user.username, movie=int(arg[2:]))
        mem.delete()
        return redirect('lists', typ='tw')
    elif arg[:2]=='wa':
        mem=Watched.objects.get(user=request.user.username, movie=int(arg[2:]))
        mem.delete()
        return redirect('lists', typ='wa')
    elif arg[:2]=='li':
        mem=Liked.objects.get(user=request.user.username, movie=int(arg[2:]))
        mem.delete()
        return redirect('lists', typ='li')

#To add or remove titles from your list (from title page)
def add_list(request, arg):
    if not request.user.is_authenticated:
        return redirect('welcome')
    if arg[0:3]=='1tw':
        mem=Towatch.objects.get(user=request.user.username, movie=int(arg[3:]))
        mem.delete()
    elif arg[0:3]=='0tw':
        movie=Titles.objects.filter(id=int(arg[3:])).values()[0]
        mem=Towatch(user=request.user.username,name=movie['name'], year=movie['year'], movie=movie['id'])
        mem.save()
    elif arg[0:3]=='1wa':
        mem=Watched.objects.get(user=request.user.username, movie=int(arg[3:]))
        mem.delete()
    elif arg[0:3]=='0wa':
        movie=Titles.objects.filter(id=int(arg[3:])).values()[0]
        mem=Watched(user=request.user.username,name=movie['name'], year=movie['year'], movie=movie['id'])
        mem.save()
    elif arg[0:3]=='1li':
        mem=Liked.objects.get(user=request.user.username, movie=int(arg[3:]))
        mem.delete()
    elif arg[0:3]=='0li':
        movie=Titles.objects.filter(id=int(arg[3:])).values()[0]
        mem=Liked(user=request.user.username,name=movie['name'], year=movie['year'], movie=movie['id'])
        mem.save()
    return redirect('titles',id=int(arg[3:]))

#To render the home page
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('welcome')

def search(request):
    if not request.user.is_authenticated:
        return redirect('welcome')
    results=Titles.objects.filter(name__icontains=request.GET['query']).values()
    return render(request, 'search.html', {'results':results, 'query':request.GET['query']})

def lists(request, typ):
    if not request.user.is_authenticated:
        return redirect('welcome')

    usr=request.user.username
    results=None
    typ2=typ
    if typ=='tw':
        results=Towatch.objects.filter(user=usr).values('movie','year','name')
        typ='To Watch'
    elif typ=='wa':
        results=Watched.objects.filter(user=usr).values('movie','year','name')
        typ='Watched'
    elif typ=='li':
        results=Liked.objects.filter(user=usr).values('movie','year','name')
        typ='Liked'

    return render(request, 'lists.html',{'type':typ, 'user':usr, 'results':results, 'type2':typ2})

def titles(request,id):
    if not request.user.is_authenticated:
        return redirect('welcome')
    
    tw=0
    w=0
    l=0
    if Towatch.objects.filter(user=request.user.username, movie=id).exists():
        tw=1
    if Watched.objects.filter(user=request.user.username, movie=id).exists():
        w=1
    if Liked.objects.filter(user=request.user.username, movie=id).exists():
        l=1

    #Time in hours (1 unit = 2 hours)
    t=round(int(time.time())/7200)

    info=Cache.objects.filter(id=id)
    if info.exists():
        info=info.values()[0]

        if(info['time']+1>=t):
            dict_=info
            try:
                dict_['seasoninfo']=info['seasoninfo'].split('[@#]')
            except:
                dict_['seasoninfo']=None
            dict_.update({'tw':tw, 'w':w, 'l':l})
            return render(request, 'title.html', dict_)
        else:
            info=Cache.objects.get(id=id)
            info.delete()

    info=Titles.objects.filter(id=id).values()
    dict_={'title':info[0]['name'], 'cast':info[0]['cast'], 'time':t}
    dict_.update(imdb(info[0]['imdb']))
    dict_.update(rt(info[0]['rt'],info[0]['year'],info[0]['type']))
    dict_.update(mc(info[0]['mc']))

    #To find similar titles
    mlt=dict_['mlt']
    dict_.pop('mlt')
    similar={'sim1':None, 'sim1h':None,'sim2':None, 'sim2h':None,'sim3':None, 'sim3h':None, 'sim4':None, 'sim4h':None}
    i=0
    for sim in mlt:
        test=Titles.objects.filter(imdb__contains=sim['href'])
        if test.exists():
            i=i+1
            similar['sim'+str(i)]=test.values()[0]['id']
            similar['sim'+str(i)+'h']=sim['img-src']
            if i==4:
                break
    dict_.update(similar)

    dict_['id']=id
    info=Cache(**dict_)
    info.save()

    dict_.update({'tw':tw, 'w':w, 'l':l, 'id':id})
    try:
        dict_['seasoninfo']=dict_['seasoninfo'].split('[@#]')
    except:
        dict_['seasoninfo']=None

    return render(request, 'title.html', dict_)