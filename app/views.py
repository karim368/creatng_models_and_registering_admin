from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topic(request):
    dto = Topic.objects.all()
    d = {'topics':dto}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    dwo = Webpage.objects.all()
    d = {'webpages':dwo}
    return render(request,'display_webpage.html',d)

def display_records(request):
    drob = AccessRecords.objects.all()
    d = {'records':drob}
    return render(request,'display_records.html',d)