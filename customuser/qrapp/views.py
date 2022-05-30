from pickle import NONE
from django.shortcuts import render
from qrapp.models import detailsdata
from qrcode import * 
# Create your views here.


def forms(request):
       return render(
        
        request,
        "templateform.html",
        {}
       )
datals=NONE

def detailssdata(request):
    global datals
    if request.method =='POST':
        name = request.POST.get('name')
        email=request.POST.get('email')
        contact= request.POST.get('contact')
        # image =request.POST.get('myfile')
        address = request.POST.get('address')
        services = request.POST.get('services')
        
        en= detailsdata(name=name, email=email,contact=contact,address=address,services=services)
       

        en.save()
        # print(en)
        print("----------------------------------------------------------------------------------------------datasaved  ")

        # datals = detailsdata.objects.all()
        datals ={"Name: ": en.name,"Contact : ": en.contact , "Address: " : en.address,"Services: ": en.services}
        # print(datals[0].name)
        print(datals)
        img = make(datals)
        img.save("static/image/test.png")
        print("-----imgaesaved")


    return render(request,'templateform.html',{'datals':datals})