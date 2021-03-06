from rest_framework import serializers
from opcapp.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCampaign
        fields = '__all__'


class ActivityNarrativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityNarrative
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class KeyConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyConcept
        fields = '__all__'


#class RoleCampaignSerializer(serializers.ModelSerializer):
 #   class Meta:
 #       model = RoleCampaign
 #       fields = '__all__'

        
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

class NeighborhoodVeredaSerializer(serializers.ModelSerializer):
    class Meta:
        model = NeighborhoodVereda
        fields = ['id', 'name', 'comunaCorregimiento', 'zone']


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class PersonCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonCampaign
        fields = '__all__'

        
