from rest_framework import serializers
from .models import (RoleUser, Gender,HigherLevelEducation, AchievedLevel)


class RoleUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RoleUser
        fields = ['id', 'name']


class GenderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'typeGender']


    

class HigherLevelEducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HigherLevelEducation
        fields = ['id', 'name']



class AchievedLevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AchievedLevel
        fields = ['id', 'name']