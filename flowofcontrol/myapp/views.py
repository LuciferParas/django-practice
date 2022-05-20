from dataclasses import dataclass
from django.shortcuts import render

# Create your views here.

def home(request):
    data = [x for x in range(1,32) ]
    return render(
        
        request,
        "home.html",
        {
            "collection" : data
        }
        
        
        
        
    )