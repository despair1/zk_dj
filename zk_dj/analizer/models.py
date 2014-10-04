from django.db import models

# Create your models here.
class pilot(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    corp=models.ForeignKey("corp",related_name="pilots",
                           null=True, default=None,
                           on_delete=models.SET_NULL)
    
class corp(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    