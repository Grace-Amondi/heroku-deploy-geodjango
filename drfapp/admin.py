# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Constituency


# customize header
admin.site.site_header = 'My Constituencies API'


# set title
admin.site.site_title= 'Admin'
admin.site.index_title= 'My Constituencies API'


class ConstituencyAdmin(admin.ModelAdmin):
    list_filter = ('COUNTY_NAM',)
    search_fields = ['CONSTITUEN','COUNTY_NAM']


# register models
admin.site.register(Constituency,ConstituencyAdmin)