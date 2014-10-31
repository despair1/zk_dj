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

from num_mates import num_mates
from analizer.new_views._time_slice import time_slice
from analizer.new_views._mates_page import mates_page
from ship_type import ship_types
from solar_systems import solar_systems
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
    #pilot1["last_kill_time"]=kill.objects.filter(characterID=pilot_id).order_by("-killTime")[0].killTime
    
    
    time_slice1=time_slice(pilot_id, date.today()-delta)
    mates,mates_pages=mates_page(request,pilot_id)
    number_mates=num_mates(pilot_id, date.today()-delta)
    attacker_ships=ship_types(pilot_id, date.today()-delta)
    solar_system_kills=solar_systems(pilot_id, date.today()-delta)
    #print attacker_ships
    #pilot1["id"]=pilot_id
    return render(request,"analizer/pilot_detail1.html",
                  {"pilot":pilot1,
                   "time_slice":time_slice1,
                   "mates":mates,
                   "mates_pages":mates_pages,
                   "number_mates": number_mates,
                   "attacker_ships": attacker_ships,
                   "solar_system_kills":solar_system_kills,
                   
                   })    