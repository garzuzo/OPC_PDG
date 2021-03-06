from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#If you don’t specify primary_key=True for any fields in your model, 
#Django will automatically add an IntegerField to hold the primary key

#It doesn’t matter which model has the ManyToManyField, 
#but you should only put it in one of the models – not both.

EDUCATION_LEVELS= (
    ('Primaria', 'Primaria'),
    ('Secundaria','Secundaria'),
    ('Tecnico/Tecnologo','Tecnico/Tecnologo'),
    ('Universitaria','Universitaria')

)

GENDER_LIST= (
    ('Femenino', 'Femenino'),
    ('Masculino','Masculino'),
    ('Intersexual','Intersexual'),

)

ZONE_LIST= (
    ('Rural', 'Rural'),
    ('Urbana','Urbana')

)

class HigherLevelEducation(models.Model):
    name=models.CharField(max_length=30, choices=EDUCATION_LEVELS)
    def __str__(self):
        return self.name

class AchievedLevel(models.Model):
    name=models.CharField(max_length=30)
    higherLevelEducation=models.ForeignKey(HigherLevelEducation, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class RoleUser(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name




class Gender(models.Model):
    typeGender=models.CharField(max_length=30)
    def __str__(self):
        return self.typeGender




#class RoleCampaign(models.Model):
 #   name=models.CharField(max_length=30)
 #   def __str__(self):
 #       return self.name



class Zone(models.Model):
    zoneType=models.CharField(max_length=30, choices=ZONE_LIST)
    def __str__(self):
        return self.zoneType

class Country(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class State(models.Model):
    name=models.CharField(max_length=60)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class City(models.Model):
    name=models.CharField(max_length=40)
    state=models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ComunaCorregimiento(models.Model):
    name=models.CharField(max_length=60)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class NeighborhoodVereda(models.Model):
    name=models.CharField(max_length=60)
    comunaCorregimiento=models.ForeignKey(ComunaCorregimiento, on_delete=models.CASCADE, blank= True)
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE)
    def __str__(self):
        return self.name



class Person(models.Model):
    birthdate=models.DateField()
    achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    neighborhoodVeredaSource=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personterritorysource', blank= True)
    neighborhoodVeredaActual=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personterritoryactual', blank= True)
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    roleUser=models.ForeignKey(RoleUser, on_delete=models.CASCADE)




class Campaign(models.Model):
    startDate=models.DateField()
    endDate=models.DateField()
    description=models.CharField(max_length=200)
    title=models.CharField(max_length=70)
    narrativesGoal=models.IntegerField()
    accumulatedNarratives=models.IntegerField()
    isActive=models.BooleanField(default=False)
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class PersonCampaign(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
   # roleCampaign=models.ForeignKey(RoleCampaign, on_delete=models.CASCADE)
    campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)
    achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    neighborhoodVeredaSource=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personcampaignterritorysource')
    neighborhoodVeredaActual=models.ForeignKey(NeighborhoodVereda, on_delete=models.CASCADE,related_name='personcampaignterritoryactual')



class Topic(models.Model):
    concepts=models.CharField(max_length=600)
    
    def __str__(self):
        return self.id


class ActivityNarrative(models.Model):
    text=models.CharField(max_length=200)
    #created_date = models.DateTimeField(default=timezone.now)
    campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)
    personCampaign=models.OneToOneField(PersonCampaign, on_delete=models.CASCADE)
    topicPrimary=models.ForeignKey(Topic, on_delete=models.CASCADE,related_name='narrativetopicprimary')
    topicSecondary=models.ForeignKey(Topic, on_delete=models.CASCADE,related_name='narrativetopicsecondary')


class KeyConcept(models.Model):
    name=models.CharField(max_length=30)
    frequency=models.IntegerField()
    activityNarrative=models.ManyToManyField(ActivityNarrative)
    def __str__(self):
        return self.name

        
class Group(models.Model):
    name=models.CharField(max_length=30)
    pin=models.CharField(max_length=10)
    campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)
    def __str__(self):
        return self.name    

class Participant(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    personCampaign=models.OneToOneField(PersonCampaign,on_delete=models.CASCADE)