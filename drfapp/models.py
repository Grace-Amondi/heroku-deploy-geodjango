# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.contrib.postgres.fields import HStoreField
from django.urls import reverse
from django.db.models import Manager as GeoManager

# constituency class
class Constituency(models.Model):
    CONSTITUEN = models.CharField(null=False,max_length = 255)
    CONST_CODE = models.FloatField(null=True)
    COUNTY_NAM = models.CharField(null=True,max_length = 255)
    Shape_Leng = models.FloatField(null=True)
    Shape_Area = models.FloatField(null=True)
    COUNTY_COD = models.FloatField(null=True)


    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField(null=True)
    def __str__(self):
        return self.CONSTITUEN


class Link(models.Model):
    """
    Metadata is stored in a PostgreSQL HStore field, which allows us to
    store arbitrary key-value pairs with a link record.
    """
    metadata = HStoreField(blank=True, null=True, default=dict)
    geo = models.LineStringField()
    objects = GeoManager()