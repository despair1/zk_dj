'''
Created on Oct 8, 2014

@author: despair1
'''

from analizer.models import kill,attacker
from django.db import transaction

@transaction.atomic()
def db_add_json(kills_data):
    ac=0
    for k in kills_data:
        if not kill.objects.filter(killID=k["killID"]).exists():
            kk=kill(killID=k["killID"],
                    killTime=k["killTime"],
                    solarSystemID=k["solarSystemID"],
                    corporationName=k["victim"]["corporationName"],
                    characterName=k["victim"]["characterName"],
                    allianceName=k["victim"]["allianceName"],
                    corporationID=k["victim"]["corporationID"],
                    allianceID=k["victim"]["allianceID"],
                    characterID=k["victim"]["characterID"],
                    )
            kk.save()
            for a in k["attackers"]:
                ac+=1
                aa=attacker(corporationID=a["corporationID"],
                            allianceID=a["allianceID"],
                            characterID=a["characterID"],
                            killID=kk,
                            securityStatus=a["securityStatus"],
                            weaponTypeID=a["weaponTypeID"],
                            finalBlow=a["finalBlow"],
                            shipTypeID=a["shipTypeID"],
                            corporationName=a["corporationName"],
                            characterName=a["characterName"],
                            allianceName=a["allianceName"],
                            killTime=k["killTime"]
                            )

                aa.save()
    print "ac ",ac


