'''
Created on Sep 27, 2014

@author: despair1
'''

from django.shortcuts import render
from django.http import HttpResponse

def list_pilots(request):
    names_list=request.POST["names"].split("  ")
    if names_list and names_list[0]:
        return render(request,"analizer/pilots_list.html",{"pilots":names_list,
                                                           })
        return HttpResponse(" Yon in pilots list stub")
    else:
        return render(request,"analizer/index.html",{"error_message":
                                                     "Absent pilots names",
                                                     })
        
