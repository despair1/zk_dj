'''
Created on Oct 4, 2014

@author: despair1
'''
from django.db import transaction
from django.utils import timezone
from analizer.models import kill,pilot,corp,attacker,alli


    

@transaction.atomic()
def add_json2db(kills_data,pilot_id=None,corp_id=None):
    if not pilot_id and not corp_id : return
    if pilot_id:
        t=pilot.objects.get(id=pilot_id).cached
        if not t:
            def check_x_update_time(kill):
                return True
        else:
            def check_x_update_time(kill,x=t):
                return kill["killTime"]>t
    b_pilots={}
    for p in pilot.objects.all():
        b_pilots[p.id]=p
    s_pilots=[]
    b_corps={}
    for c in corp.objects.all():
        b_corps[c.id]=c
    s_corps=[]
    ac=0
    for k in kills_data:
        if not check_x_update_time(k):
            break
        if not kill.objects.filter(killID=k["killID"]).exists():
            pid=int(k["victim"]["characterID"])
            if pid in b_pilots:
                p=b_pilots[pid]
            else:
                p=pilot(id=k["victim"]["characterID"],
                      name=k["victim"]["characterName"],)
                s_pilots.append(p)
                b_pilots[pid]=p
            cid=int(k["victim"]["corporationID"])
            if cid in b_corps:
                c=b_corps[cid]
            else:             
                c=corp(id=k["victim"]["corporationID"],
                     name=k["victim"]["corporationName"],)
                s_corps.append(c)
                b_corps[cid]=c
            """
            if int(k["victim"]["allianceID"]):
                a=alli(allianceID=k["victim"]["allianceID"],
                       allianceName=k["victim"]["allianceName"],)
                a.save()
            else:
                a=None
            p.save()
            c.save()
            """
            a=None
            #my_datetime = timezone.make_aware(k["killTime"], timezone.get_current_timezone())
            kk=kill(killID=k["killID"],
                    killTime=k["killTime"],
                    solarSystemID=k["solarSystemID"],
                    corporationName=k["victim"]["corporationName"],
                    characterName=k["victim"]["characterName"],
                    allianceName=k["victim"]["allianceName"],
                    corporationID=c,
                    allianceID=a,
                    characterID=p,
                    )
            kk.save()

            for a in k["attackers"]:
                """
                p=pilot(id=a["characterID"],
                      name=a["characterName"],)
                c=corp(id=a["corporationID"],
                     name=a["corporationName"],)
                p.save()
                c.save()
                if int(a["allianceID"]):
                    al=alli(allianceID=a["allianceID"],
                           allianceName=a["allianceName"],)
                    al.save()
                else:
                    al=None
                 """
                ac+=1
                pid=int(a["characterID"])
                if pid in b_pilots:
                    p=b_pilots[pid]
                else:
                    p=pilot(id=a["characterID"],
                          name=a["characterName"],)
                    s_pilots.append(p)
                    b_pilots[pid]=p
                cid=int(a["corporationID"])
                if cid in b_corps:
                    c=b_corps[cid]
                else:             
                    c=corp(id=a["corporationID"],
                         name=a["corporationName"],)
                    s_corps.append(c)
                    b_corps[cid]=c
                al=None
                
                aa=attacker(corporationID=c,
                            allianceID=al,
                            characterID=p,
                            killID=kk,
                            securityStatus=a["securityStatus"],
                            weaponTypeID=a["weaponTypeID"],
                            finalBlow=a["finalBlow"],
                            shipTypeID=a["shipTypeID"],
                            corporationName=a["corporationName"],
                            characterName=a["characterName"],
                            allianceName=a["allianceName"],
                            )

                aa.save()
    pilot.objects.bulk_create(s_pilots)
    corp.objects.bulk_create(s_corps)
    print "ac ",ac
    


        
    