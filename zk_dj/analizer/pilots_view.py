'''
Created on Sep 27, 2014

@author: despair1
'''

from django.shortcuts import render
from django.http import HttpResponse
from analizer.tools import character_id
from analizer.models import pilot
import re 
from analizer.tools.db_get_pilot import get_pilot_from_db

def list_pilots(request):
    names_list=request.POST["names"]
    #names_list=re.sub(r"&#\w\w;","  ",names_list)
    #names_list=names_list.rstrip()
    s=names_list.replace("\r\n","  ")
    names_list=s.split("  ")
    print "names list",names_list
    t=[]
    for name in names_list:
        if not name: continue
        d={}
        d["name"]=name
        if get_pilot_from_db(d):
            """TODO add kills attackers to search
            """
            t.append(d)
            continue
        else:
            """
        id1=0
        pilots_list=pilot.objects.filter(name__iexact=name)
        #pilot.objects.filter(pk=0).delete()
        if len(pilots_list)==1:
            id1=pilots_list[0].id
            d["name"]=pilots_list[0].name
            c=pilots_list[0].corp
            if c:
                print c.name,c.id
                d["corp_name"]=c.name
                d["corp_id"]=c.id
                """
        
        #else:
            pilots_list=character_id.get_id_by_pilot_name(name)
            for i1 in pilots_list:
                if i1["name"].upper()== name.upper():
                    id1=int(i1["characterID"])
                    d["name"]=i1["name"]
                    if int(id1):
                        pilot(name=i1["name"],id=id1).save()
                        d["id"]=id1
                        t.append(d)
                    break
            
        """            
        if int(id1):
            d["id"]=id1
            t.append(d) """
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
        
