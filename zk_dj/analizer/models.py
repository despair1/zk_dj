from django.db import models

# Create your models here.
class pilot(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    cached=models.DateTimeField(null=True, default=None)
    
class corp(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    cached=models.DateTimeField(null=True, default=None)
    
class alli(models.Model):
    allianceID=models.IntegerField(primary_key=True)
    allianceName=models.CharField(max_length=255)
    cached=models.DateTimeField(null=True, default=None)
    
"""_____ attacker  {u'corporationID': 98341562, u'factionID': 0, u'securityStatus': 5,
 u'weaponTypeID': 7171, u'characterName': u'Rhamos', u'factionName': u'',
  u'allianceName': u'Knights of Tomorrow', u'finalBlow': 1, u'allianceID': 99000679,
   u'shipTypeID': 4302, u'corporationName': u'1UltraNova1', u'characterID': 1000551122, u'damageDone': 7692} """
   
class attacker(models.Model):
    corporationID=models.IntegerField()
    allianceID=models.IntegerField()
    characterID=models.IntegerField()
    killID=models.ForeignKey("kill",related_name="kills")
    securityStatus=models.FloatField()
    weaponTypeID=models.IntegerField()
    finalBlow=models.IntegerField()
    shipTypeID=models.IntegerField()
    corporationName=models.CharField(max_length=255)
    characterName=models.CharField(max_length=255,null=True)
    allianceName=models.CharField(max_length=255,null=True)
    killTime=models.DateTimeField()
    
""" keys  [u'killID', u'killTime', u'zkb', u'attackers', u'victim', u'items', u'solarSystemID', u'moonID']
 key  victim
{u'corporationID': 98288825, u'factionID': 0, u'damageTaken': 7906,
 u'characterName': u'Eligh Douglas', u'factionName': u'', u'allianceName': u'',
  u'allianceID': 0, u'shipTypeID': 17478, u'corporationName': u'The Big Love', u'characterID': 94883185}
""" 
class kill(models.Model):
    killID=models.IntegerField(primary_key=True)
    killTime=models.DateTimeField()
    solarSystemID=models.IntegerField()
    corporationName=models.CharField(max_length=255)
    characterName=models.CharField(max_length=255,null=True)
    allianceName=models.CharField(max_length=255,null=True)
    corporationID=models.IntegerField()
    allianceID=models.IntegerField()
    characterID=models.IntegerField()