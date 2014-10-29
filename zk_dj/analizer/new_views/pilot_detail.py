'''
Created on Oct 25, 2014

@author: despair1
'''
#import sys
#sys.path.append("/home/despair1/git/czk/2/bpczk/Debug")
from test2 import tt
#from json_kills.time1 import time_slice
base_request="https://zkillboard.com/api/"
from datetime import timedelta,date
from analizer.tools.db_get_pilot import get_pilot_by_id

from django.shortcuts import render,Http404
from analizer.models import kill,attacker
from django.db import connection
sign_kill=2
mates_per_page=15
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from analizer.new_views._num_mates import num_mates
from analizer.new_views._time_slice import time_slice
def pilot_detail(request,pilot_id):
    pilot1=get_pilot_by_id(pilot_id)
    if not pilot1: raise Http404
    req=base_request+"characterID/"+str(pilot_id)+"/"
    delta=timedelta(days=90)
    delta1=timedelta(days=9)
    req=req+"startTime/"+(date.today()-delta).strftime("%Y%m%d0000")+"/"
    #tt(req)
    #print kill.objects.filter(characterID=pilot_id).filter(killTime__gt=date.today()-delta1).count()
    pilot1["number_kills"]=attacker.objects.filter(characterID=pilot_id).filter(killTime__gt=date.today()-delta1).count()
    pilot1["number_loss"]=kill.objects.filter(characterID=pilot_id).filter(killTime__gt=date.today()-delta1).count()
    #if pilot1["number_loss"]>0 or pilot1["number_kills"]>0:
    pilot1["last_kill_time"]=kill.objects.filter(characterID=pilot_id).order_by("-killTime")[0].killTime
    
    cursor = connection.cursor() 
    time_slice1=time_slice(pilot_id, date.today()-delta)
    
        #print i
    cursor.execute("""select "characterID","characterName",count(*) as cnt from analizer_attacker 
    where "characterID" <> %s and "characterID" <> 0 and
    "killID_id" in     (select "killID_id" from analizer_attacker where "characterID"=%s)
     
    group by "characterID","characterName" order by count(*) desc;
    """,[pilot_id,pilot_id])
    r=cursor.fetchall()
    p=Paginator(r,mates_per_page)
    mate_page = request.GET.get('mate_page', 1)
    try:
        page=p.page(mate_page)
    except PageNotAnInteger:
        page=p.page(1)
    except EmptyPage:
        page=p.page(p.num_pages)
    mates=[]
    for i in page.object_list:
        d=get_pilot_by_id(i[0])
        #if int(i[0])==int(pilot_id): continue
        d["id"]=i[0]
        d["name"]=i[1]
        d["kills"]=i[2]
        #print d
        mates.append(d)
    mates_pages={}
    mates_pages["pilot"]=pilot_id
    if page.has_next():
        mates_pages["next"]=page.next_page_number()
    if page.has_previous():
        mates_pages["prev"]=page.previous_page_number()
        #print d
    
    #pilot1["id"]=pilot_id
    return render(request,"analizer/pilot_detail1.html",
                  {"pilot":pilot1,
                   "time_slice":time_slice1,
                   "mates":mates,
                   "mates_pages":mates_pages,
                   
                   })    