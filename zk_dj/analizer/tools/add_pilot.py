'''
Created on Oct 4, 2014

@author: despair1
'''
from analizer.models import pilot,kill,corp

def add_pilot_corp(kill1):
    
    try:
        pilot.objects.get(id=kill1.characterID)
    except pilot.DoesNotExist:
        pass
        