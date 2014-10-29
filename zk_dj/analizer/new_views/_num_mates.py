'''
Created on Oct 29, 2014

@author: despair1
'''

from django.db import connection

def num_mates(pilot_id,start_time):
    cursor = connection.cursor()
    cursor.execute("""select "killID_id",count(*) as cnt from analizer_attacker 
    where  "killTime" > %s and
    "killID_id" in ( select "killID_id" from analizer_attacker where "characterID"=%s)    
    group by "killID_id" ;
    """,[start_time,pilot_id])
    r=cursor.fetchall()
    d={}
    d["solo"]=0
    d["5"]=0
    d["15"]=0
    d["35"]=0
    d["blob"]=0
    for i in r:
        #print i[0],i[1]
        if i[1]==1: d["solo"]+=1
        elif i[1]<6 : d["5"]+=1
        elif i[1]<16 : d["15"]+=1
        elif i[1]<36 : d["35"]+=1
        else : d["blob"]+=1
    return d