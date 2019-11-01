from rest_framework import serializers
from opcapp.models import (RoleUser, Gender, HigherLevelEducation, AchievedLevel,Country, State, City, ComunaCorregimiento, NeighborhoodVereda, Zone, Campaign, ActivityNarrative, Concept, KeyConcept)


class RoleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUser
        fields = ['id', 'name']


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ['id', 'typeGender']


    

class HigherLevelEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HigherLevelEducation
        fields = ['id', 'name']



class AchievedLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievedLevel
        fields = ['id', 'name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']




class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'name', 'country']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'state']


class ComunaCorregimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComunaCorregimiento
        fields = ['id', 'name', 'city', 'zone']

class ZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = ['id', 'zoneType']

ActivityNarrative
class NeighborhoodVeredaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighborhoodVereda
        fields = ['id', 'name', 'comunaCorregimiento', 'zone']


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'startDate', 'endDate', 'description', 'title', 'narrativesGoal', 'accumulatedNarratives', 'isActive']


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = '__all__'

class ActivityNarrativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityNarrative
        fields = '__all__'


class KeyConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyConcept
        fields = '__all__'

        
