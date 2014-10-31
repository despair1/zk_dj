'''
Created on Oct 31, 2014

@author: despair1
'''

from django.db import connection
from eve_db.models import Mapsolarsystems

def solar_systems(pilot_id,start_time):
    cursor = connection.cursor()
    cursor.execute("""select "solarSystemID",count(*) as cnt from analizer_kill 
    where  
    "killID" in ( select "killID_id" from analizer_attacker 
        where "killTime" > %s and "characterID"=%s)    
    group by "solarSystemID" order by cnt desc limit 15;
    """,[start_time,pilot_id])
    r=cursor.fetchall()
    ssk=[]
    for i in r:
        d={}
        d["solar_system_name"]=Mapsolarsystems.objects.using("eve_db").get(solarsystemid=i[0]).solarsystemname
        d["kills"]=i[1]
        #print i[0],i[1],Mapsolarsystems.objects.using("eve_db").get(solarsystemid=i[0]).solarsystemname
        ssk.append(d)
    return ssk
