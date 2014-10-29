'''
Created on Oct 29, 2014

@author: despair1
'''

from django.db import connection

def num_mates(pilot_id,kill_time):
    cursor = connection.cursor()
    cursor.execute("""select "killID_id",count(*) as cnt from analizer_attacker 
    where "characterID" = %s and "killTime" > %s    
    group by "killID_id" ;
    """,[pilot_id,kill_time])
    r=cursor.fetchall()
    d={}
    d["solo"]=0
    d["5"]=0
    d["15"]=0
    d["35"]=0
    d["blob"]=0
    for i in r:
        if i[1]==1: d["solo"]+=1
        elif i[1]<6 : d["5"]+=1
        elif i[1]<16 : d["15"]+=1
        elif i[1]<36 : d["35"]+=1
        else : d["blob"]+=1
    return d