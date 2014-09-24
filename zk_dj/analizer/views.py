from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request,"analizer/index.html",{"error_message1":"",
                                                 }) 
    return HttpResponse("you in index")
def list_names(request):
    return HttpResponse("you in list")