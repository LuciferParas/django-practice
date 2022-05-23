from pickle import NONE
from django.shortcuts import render
from qrapp.models import detailsdata
from qrcode import * 
# Create your views here.


def home(request):
       return render(
        
        request,
        "home.html",
        {}
       )
datals=NONE

def detailssdata(request):
    global datals
    if request.method =='POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        contact= request.POST.get('contact')

        en= detailsdata(name=name, email=email,contact=contact)
       

        en.save()
        print(en)
        print("----------------------------------------------------------------------------------------------datasaved  ")

        datals = detailsdata.objects.all()
        # print(datals)
        img = make(datals)
        img.save("static/image/test.png")


    return render(request,'home.html',{'datals':datals})