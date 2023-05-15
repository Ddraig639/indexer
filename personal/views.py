from django.shortcuts import render
import os
from .models import Movie
# Create your views here.

def screener(movie):
    before=0
    temp=""
    for i in movie:
        if i.isdigit():
            temp=temp+i
            before=before+1
        else:
            before=0
            temp=""
        if before==4:
            break
    if len(temp)==4:
        return temp
    else:
        return 0

def movieprs(request):
    thislist = []
    path = str(request.POST.get('movie'))
    dir_list = os.listdir(path)
    for i in dir_list:
        thislist.append(Movie(username=str(i), mdate=screener(str(i))))
    for x in thislist:
        x.save()
    content={}
    movielist=Movie.objects.all().order_by('mdate').values
    #movielist.sort('mdate')
    content['allm']=movielist
    return render(request, 'personal/moviedis.html', content)

def movieadd(request):
    x = Movie.objects.all()
    x.delete()
    return render(request, 'personal/movieadd.html', {})

