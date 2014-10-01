'''
Created on Sep 24, 2014

@author: despair1
'''

from analizer import views

from django.conf.urls import patterns, url

urlpatterns=(url(r"^$",views.index,name="index"),
             url(r"^list/",views.list_names,name="list"),
             url(r"^pilot_detail/(?P<id>[0-9]+)/",
                 views.pilot_detail,name="pilot_detail")
             )



