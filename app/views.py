from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse("Topic is created")
    return render(request,"insert_topic.html",d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            print(WFDO.cleaned_data)
            tn=WFDO.cleaned_data['topic_name']
            nm=WFDO.cleaned_data['name']
            email=WFDO.cleaned_data['email']
            url=WFDO.cleaned_data['url']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=nm,url=url,email=email)[0]
            WO.save()
            return HttpResponse("Webpage is created")
        else:
            return HttpResponse("Invalid data")
    return render(request,"insert_webpage.html",d)

def insert_accessrecord(request):
    d={'EAFO':AccessRecordForm()}
    if request.method=="POST":
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            nm=AFDO.cleaned_data['name']
            au=AFDO.cleaned_data['author']
            date=AFDO.cleaned_data['date']
            WO=Webpage.objects.get(name=nm)
            AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=date)[0]
            AO.save()
            return HttpResponse('Accessrecord is created')
        else:
            return HttpResponse('Invalid data')
    return render(request,"insert_accessrecord.html",d)