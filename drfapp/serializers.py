from rest_framework import serializers
from django.contrib.auth.models import User, Group
from drfapp.models import Constituency
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):


     class Meta:
        model = User
        fields = ('username', 'id', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Group
        fields = ('id', 'name')


class ConstituencySerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Constituency
        fields =   ('COUNTY_COD','CONST_CODE','CONSTITUEN','COUNTY_NAM','Shape_Leng','Shape_Area','mpoly')