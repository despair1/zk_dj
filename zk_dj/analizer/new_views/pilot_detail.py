'''
Created on Oct 25, 2014

@author: despair1
'''
#import sys
#sys.path.append("/home/despair1/git/czk/2/bpczk/Debug")
from test2 import tt
base_request="https://zkillboard.com/api/"
from datetime import timedelta,date
from analizer.tools.db_get_pilot import get_pilot_by_id

from django.shortcuts import render,Http404
from analizer.models import kill,attacker
from django.db import connection
sign_kill=2

def pilot_detail(request,pilot_id):
    pilot1=get_pilot_by_id(pilot_id)
    if not pilot1: raise Http404
    req=base_request+"characterID/"+str(pilot_id)+"/"
    delta=timedelta(days=90)
    delta1=timedelta(days=9)
    req=req+"startTime/"+(date.today()-delta).strftime("%Y%m%d0000")+"/"
    #tt(req)
    print kill.objects.filter(characterID=pilot_id).filter(killTime__gt=date.today()-delta1).count()
    pilot1["number_kills"]=attacker.objects.filter(characterID=pilot_id).filter(killTime__gt=date.today()-delta1).count()
    pilot1["number_loss"]=kill.objects.filter(characterID=pilot_id).filter(killTime__gt=date.today()-delta1).count()
    #if pilot1["number_loss"]>0 or pilot1["number_kills"]>0:
    pilot1["last_kill_time"]=kill.objects.filter(characterID=pilot_id).order_by("-killTime")[0].killTime
    cursor = connection.cursor()
    cursor.execute("""select extract( hour from "killTime" ) as a1,count(*) as cnt from analizer_kill
    where "characterID"=%s  group by a1 having count(*)>%s order by cnt desc;""",[pilot_id,sign_kill])
    r=cursor.fetchall()
    ts=[]
    for i in r:
        d={}
        d["hour"]=int(i[0])
        d["kills"]=i[1]
        ts.append(d)
        #print i
    
    #pilot1["id"]=pilot_id
    return render(request,"analizer/pilot_detail1.html",
                  {"pilot":pilot1,
                   "time_slice":ts,
                   
                   })    