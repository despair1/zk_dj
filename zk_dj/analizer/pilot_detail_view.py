'''
Created on Oct 2, 2014

@author: despair1
'''

from django.shortcuts import render,get_object_or_404
from models import pilot,corp,kill
from tools.get_json import get_json_pilot
from json_kills import json_utils
from django.db import transaction
from tools.json2db import add_json2db
from profiling import profile
import sys
from django.http import Http404
from analizer.tools.db_get_pilot import get_pilot_by_id
#from analizer.tools.db_add_json import db_add_json
#from web_test.pilot_header1 import html_kills_loss_time
import hotshot
def profile(log_file):
    
    def _outer(f):
        def _inner(*args, **kwargs):
            
            
            

            prof = hotshot.Profile(log_file)
            try:
                ret = prof.runcall(f, *args, **kwargs)
            finally:
                prof.close()
            return ret

        return _inner
    return _outer


class twrite():
    def __init__(self):
        self.f=open("/tmp/t_tstats","w")
    def write(self,s):
        print s
        self.f.write(s)
    def __del__(self):
        self.f.close()

def get_victim_list(kills_data):
    victim_list=[]
    for i in kills_data:
        victim={}
        victim["pilot_id"]=i["victim"]["characterID"]
        victim["pilot_name"]=i["victim"]["characterName"]
        victim["corp_name"]=i["victim"]["corporationName"]
        victim["ship_type"]=i["victim"]["shipTypeID"]
        victim["kill_time"]=i["killTime"]
        victim_list.append(victim)
    return victim_list
@transaction.atomic()
def add_pilots_corps_to_db(kills_data):
    for i in reversed(kills_data):
        if int(i["victim"]["characterID"]) and int(i["victim"]["corporationID"]):
            c=corp(id=i["victim"]["corporationID"],
                 name=i["victim"]["corporationName"])
            c.save()
            pilot(id=i["victim"]["characterID"],
                  name=i["victim"]["characterName"],
                  corp=c).save()
            
#@profile(stats=True, stats_buffer=twrite())
@profile("myprof")
def pilot_detail(request,pilot_id):
    print "in detail"
    pilot1=get_pilot_by_id(pilot_id)
    if not pilot1: raise Http404
    #pilot1["id"]=pilot_id
    name=get_object_or_404(pilot,id=pilot_id)
    #name=pilot.objects.filter(pk=pilot_id)
    #pilot1["name"]=name.name
    print "get json"
    kills_data=get_json_pilot(characterID=pilot_id)
    print "add_json"
    #db_add_json(kills_data)
    #add_pilots_corps_to_db(kills_data)
    print "add_json1"
    #add_json2db(kills_data,pilot_id=pilot_id)
    
    kills,loss=json_utils.divide_kill_lose(pilotID=pilot_id, kills_data=kills_data)
    pilot1["number_kills"]=len(kills)
    pilot1["number_loss"]=len(loss)
    pilot1["last_kill_time"]=json_utils.get_last_kill_time(kills_data=kills_data)
    loss=kill.objects.filter(characterID=pilot_id)
    print "pre render"
    return render(request,"analizer/pilot_detail.html",
                  {"pilot":pilot1,
                   "victim_list":get_victim_list(kills_data),
                   "loss":loss,
                   })    