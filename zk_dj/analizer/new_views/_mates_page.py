'''
Created on Oct 29, 2014

@author: despair1
'''

from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
mates_per_page=15
from analizer.tools.db_get_pilot import get_pilot_by_id

def mates_page(request,pilot_id):
    cursor = connection.cursor() 
    cursor.execute("""select "characterID","characterName",count(*) as cnt from analizer_attacker 
    where "characterID" <> %s and "characterID" <> 0 and
    "killID_id" in     (select "killID_id" from analizer_attacker where "characterID"=%s)
     
    group by "characterID","characterName" order by count(*) desc;
    """,[pilot_id,pilot_id])
    r=cursor.fetchall()
    p=Paginator(r,mates_per_page)
    mate_page = request.GET.get('mate_page', 1)
    try:
        page=p.page(mate_page)
    except PageNotAnInteger:
        page=p.page(1)
    except EmptyPage:
        page=p.page(p.num_pages)
    mates=[]
    for i in page.object_list:
        d=get_pilot_by_id(i[0])
        #if int(i[0])==int(pilot_id): continue
        d["id"]=i[0]
        d["name"]=i[1]
        d["kills"]=i[2]
        #print d
        mates.append(d)
    mates_pages={}
    mates_pages["pilot"]=pilot_id
    if page.has_next():
        mates_pages["next"]=page.next_page_number()
    if page.has_previous():
        mates_pages["prev"]=page.previous_page_number()
    return mates,mates_pages