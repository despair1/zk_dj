'''
Created on Oct 8, 2014

@author: despair1
'''
from analizer.models import pilot,kill,attacker
def get_pilot_from_db(s_pilot):
    pilot1=pilot.objects.filter(name__iexact=s_pilot["name"])
    if len(pilot1)==1:
        s_pilot["name"]=pilot1[0].name
        s_pilot["id"]=pilot1[0].id
        return True
    return None

def get_pilot_by_id(id1):
    k=kill.objects.order_by("-killTime").filter(characterID=id1)[:1]
    a=attacker.objects.order_by("-killTime").filter(characterID=id1)[:1]
    if len(a) and len(k):
        if k[0].killTime<a[0].killTime:
            k=a
    else:
        if not len(k):
            k=a
    pilot1={}
    if len(k):
        
        pilot1["pilot_name"]=k[0].characterName
        pilot1["pilot_id"]=k[0].characterID
        pilot1["corp_name"]=k[0].corporationName
        pilot1["corp_id"]=k[0].corporationID
        return pilot1
    else:
        pilot2=pilot.objects.filter(id=id1)
        if len(pilot2)==1:
            pilot1["pilot_name"]=pilot2[0].name
            pilot1["pilot_id"]=pilot2[0].id
            return pilot1
    return None
        