from django.db import models
from django.utils import timezone
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
    ('M', 'Masculino'),
    ('F','Femenino')

)



class HigherLevelEducation(models.Model):
    name=models.CharField(max_length=30, choices=EDUCATION_LEVELS)

#class HigherLevelEducationAchievedLevel(models.Model):
#    higherLevelEducation=models.ForeignKey(HigherLevelEducation, on_delete=models.CASCADE)
 #   achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)

class AchievedLevel(models.Model):
    name=models.CharField(max_length=30)
    higherLevelEducation=models.ManyToManyField(HigherLevelEducation)


class RoleUser(models.Model):
    name=models.CharField(max_length=30)



class User(models.Model):
    email=models.CharField(max_length=30, primary_key=True)
    password=models.CharField(max_length=30)
    phoneNumber=models.CharField(max_length=30)
    roleUser=models.ForeignKey(RoleUser, on_delete=models.CASCADE)



class Gender(models.Model):
    typeGender=models.CharField(max_length=30)





class RoleCampaign(models.Model):
    name=models.CharField(max_length=30)




class Zone(models.Model):
    zoneType=models.CharField(max_length=30)


class Country(models.Model):
    name=models.CharField(max_length=30)


class State(models.Model):
    name=models.CharField(max_length=30)
    country=models.ForeignKey(Country, on_delete=models.CASCADE)




class City(models.Model):
    name=models.CharField(max_length=30)
    state=models.ForeignKey(State, on_delete=models.CASCADE)

class ComunaCorregimiento(models.Model):
    name=models.CharField(max_length=30)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    

class NeightborhoodVereda(models.Model):
    name=models.CharField(max_length=30)
    comunaCorregimiento=models.ForeignKey(ComunaCorregimiento, on_delete=models.CASCADE)
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE)




class Person(models.Model):
   # id=models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    birthdate=models.DateField()
    achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    higherLevelEducation=models.ForeignKey(HigherLevelEducation, on_delete=models.CASCADE)
    neightborhoodVeredaSource=models.ForeignKey(NeightborhoodVereda, on_delete=models.CASCADE,related_name='personterritorysource')
    neightborhoodVeredaActual=models.ForeignKey(NeightborhoodVereda, on_delete=models.CASCADE,related_name='personterritoryactual')
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)





class Campaign(models.Model):
    #campain_id=models.CharField(max_length=30)
    startDate=models.DateTimeField(default=timezone.now)
    endDate=models.DateField()
    description=models.CharField(max_length=200)
    title=models.CharField(max_length=30)
    narrativesGoal=models.IntegerField()
    accumulatedNarratives=models.IntegerField()
    isActive=models.BooleanField(default=False)



class PersonCampaign(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    roleCampaign=models.ForeignKey(RoleCampaign, on_delete=models.CASCADE)
    campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)
    achievedLevel=models.ForeignKey(AchievedLevel, on_delete=models.CASCADE)
    gender=models.ForeignKey(Gender, on_delete=models.CASCADE)
    higherLevelEducation=models.ForeignKey(HigherLevelEducation, on_delete=models.CASCADE)
    neightborhoodVeredaSource=models.ForeignKey(NeightborhoodVereda, on_delete=models.CASCADE,related_name='personcampaignterritorysource')
    neightborhoodVeredaActual=models.ForeignKey(NeightborhoodVereda, on_delete=models.CASCADE,related_name='personcampaignterritoryactual')




class ActivityNarrative(models.Model):
    text=models.CharField(max_length=200)
    #created_date = models.DateTimeField(default=timezone.now)
    campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)

#reemplazado por models.ManyToManyField()
#class ConceptNarrative(models.Model):
 #   activityNarrative=models.ForeignKey(ActivityNarrative, on_delete=CASCADE)
  #  concept=models.ForeignKey(Concept, on_delete=CASCADE)

class Concept(models.Model):
    #id=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    frequency=models.IntegerField()
    activityNarrative=models.ManyToManyField(ActivityNarrative)

#class KeyConceptNarrative(models.Model):
 #   activityNarrative=models.ForeignKey(ActivityNarrative, on_delete=CASCADE)
  #  keyConcept=models.ForeignKey(KeyConcept, on_delete=CASCADE)

class KeyConcept(models.Model):
    #id=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    frequency=models.IntegerField()
    activityNarrative=models.ManyToManyField(ActivityNarrative)

class Group(models.Model):
    name=models.CharField(max_length=30)
    pin=models.CharField(max_length=10)
    campaign=models.ForeignKey(Campaign, on_delete=models.CASCADE)
    

class Participant(models.Model):
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    personCampaign=models.OneToOneField(PersonCampaign,on_delete=models.CASCADE)