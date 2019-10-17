from django.contrib import admin
from .models import (Person,
HigherLevelEducation,
AchievedLevel,
RoleUser,
User,
Gender,
RoleCampaign,
Zone,
Country,
State,
City,
ComunaCorregimiento,
NeightborhoodVereda,
Campaign,
PersonCampaign,
ActivityNarrative,
Concept,
KeyConcept,
Group,
Participant)
# Register your models here.


admin.site.register(HigherLevelEducation)
admin.site.register(AchievedLevel)
admin.site.register(RoleUser)
admin.site.register(User)
admin.site.register(Gender)
admin.site.register(RoleCampaign)
admin.site.register(Zone)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(ComunaCorregimiento)
admin.site.register(NeightborhoodVereda)
admin.site.register(Campaign)
admin.site.register(PersonCampaign)
admin.site.register(ActivityNarrative)
admin.site.register(Concept)
admin.site.register(KeyConcept)
admin.site.register(Group)
admin.site.register(Participant)
admin.site.register(Person)