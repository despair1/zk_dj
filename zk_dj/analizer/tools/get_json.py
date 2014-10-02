'''
Created on Oct 2, 2014

@author: despair1
'''
base_request="https://zkillboard.com/api/"
from datetime import timedelta,date
import urllib2
import json

def _get_json(delta,req):
    req=req+"startTime/"+(date.today()-delta).strftime("%Y%m%d0000")+"/"
    print req
    req=urllib2.Request(req)
    req.add_header('User-Agent', 'test_parser, eveguide0@gmail.com')
    res=urllib2.urlopen(req)
    r=res.read()
    j=json.loads(r)
    return j    

def get_json_pilot(characterID=None,delta=timedelta(days=90)):
    req=base_request
    if not characterID: return None
    req=req+"characterID/"+str(characterID)+"/"
    return _get_json(delta,req)
