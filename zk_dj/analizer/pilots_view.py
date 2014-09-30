'''
Created on Sep 27, 2014

@author: despair1
'''

from django.shortcuts import render
from django.http import HttpResponse
from eve_api import character_id

def list_pilots(request):
    names_list=request.POST["names"].split("  ")
    t=[]
    for i in names_list:
        d={}
        d["name"]=i
        id1=0
        pilots_list=character_id.get_id_by_pilot_name(i)
        for i1 in pilots_list:
            if i1["name"].upper()== i.upper():
                id1=int(i1["characterID"])
        if id1:
            d["id"]=id1
            t.append(d)
    for i in t:
        print i["name"],i["id"]
    names_list=t
    if names_list :
        return render(request,"analizer/pilots_list.html",{"pilots":names_list,
                                                           })
        return HttpResponse(" Yon in pilots list stub")
    else:
        return render(request,"analizer/index.html",{"error_message":
                                                     "Absent pilots names",
                                                     })
        
