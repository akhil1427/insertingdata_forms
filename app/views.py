from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def tables(request):
    if request.method=='POST':
        TN=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=TN)[0]
        TO.save()

        TT=Topic.objects.all()
        d={'topics':TT}
        return render(request,'insert_topic.html',d)
    return render(request,'tables.html',)

def web(request):
    WLO=Topic.objects.all()
    d={'topics':WLO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        TN=Topic.objects.get(topic_name=tn)
        WEO=Webpage.objects.get_or_create(topic_name=TN,name=na,url=ur)[0]
        WEO.save()


        WW=Webpage.objects.all()
        d1={'webpage':WW}
        return render(request,'insert_web.html',d1)
    return render(request,'web.html',d)


def access(request):
     ACCR=Webpage.objects.all()
     d={'webpage':ACCR}
     if request.method=='POST':
         na=request.POST['na']
         da=request.POST['da']
         au=request.POST['au']
         NA=Webpage.objects.get(name=na)
         ACO=AccessRecord.objects.get_or_create(name=NA,date=da,Author=au)[0]
         ACO.save()

         AC=AccessRecord.objects.all()
         d1={'access':AC}
         return render(request,'insert_access.html',d1)

     
     return render(request,'access.html',d)

