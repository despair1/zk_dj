'''
Created on Oct 29, 2014

@author: despair1
'''
sign_kill=2
from django.db import connection
def time_slice(pilot_id,start_day):
    cursor = connection.cursor()
    cursor.execute("""select extract( hour from "killTime" ) as a1,count(*) as cnt from analizer_kill
    where "characterID"=%s and "killTime">%s  
    group by a1 having count(*)>%s order by cnt desc;""",[pilot_id,start_day,sign_kill])
    r=cursor.fetchall()
    
        
    time_slice=[]
    for i in r:
        d={}
        d["hour"]=int(i[0])
        d["kills"]=i[1]
        time_slice.append(d)
    return time_slice