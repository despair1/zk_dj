'''
Created on Oct 2, 2014

@author: despair1
'''

from django.shortcuts import render,get_object_or_404
from models import pilot,corp
from tools.get_json import get_json_pilot
from json_kills import json_utils
from django.db import transaction
#from web_test.pilot_header1 import html_kills_loss_time

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
            

def pilot_detail(request,pilot_id):
    pilot1={}
    pilot1["id"]=pilot_id
    name=get_object_or_404(pilot,id=pilot_id)
    #name=pilot.objects.filter(pk=pilot_id)
    pilot1["name"]=name.name
    
    kills_data=get_json_pilot(characterID=pilot_id)
    add_pilots_corps_to_db(kills_data)
    
    kills,loss=json_utils.divide_kill_lose(pilotID=pilot_id, kills_data=kills_data)
    pilot1["number_kills"]=len(kills)
    pilot1["number_loss"]=len(loss)
    pilot1["last_kill_time"]=json_utils.get_last_kill_time(kills_data=kills_data)
    
    return render(request,"analizer/pilot_detail.html",
                  {"pilot":pilot1,
                   "victim_list":get_victim_list(kills_data)
                   })    