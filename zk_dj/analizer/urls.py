'''
Created on Sep 24, 2014

@author: despair1
'''

from analizer import views

from django.conf.urls import patterns, url

urlpatterns=(url(r"^$",views.index,name="index"),
             url(r"^list/",views.list_names,name="list"),
             )



