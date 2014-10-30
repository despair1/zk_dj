'''
Created on Oct 30, 2014

@author: despair1
'''
from django.db import connection
from eve_db.models import Invtypes

def ship_types(pilot_id,start_time):
    cursor = connection.cursor()
    cursor.execute("""select "shipTypeID",count(*) as cnt from analizer_attacker 
    where  "shipTypeID" <> 0 and
    "killID_id" in ( select "killID_id" from analizer_attacker 
        where "killTime" > %s and "characterID"=%s)    
    group by "shipTypeID" order by cnt desc;
    """,[start_time,pilot_id])
    r=cursor.fetchall()[0:15]
    ship_kills=[]
    for i in r:
        d={}
        #print i[0],i[1],Invtypes.objects.using("eve_db").get(typeid=i[0]).typename
        d["ship"]=Invtypes.objects.using("eve_db").get(typeid=i[0]).typename
        d["attacks"]=i[1]
        ship_kills.append(d)
    return ship_kills