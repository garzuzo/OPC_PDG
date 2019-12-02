from django.urls import include, path
from rest_framework import routers
from . import views
#Auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

#router.register(r'states', views.states_list)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   # path('', views.index, name='index'),

    path('gender/', views.gender),
    path('levelseducation/', views.levelseducation),

    path('levelineducation/', views.leveleducation_list),
#GET /states?country=colombia
    path('states/', views.states_list),
#GET /cities?state=escogepersona
    path('cities/', views.cities_list),
#GET /corregimientos_comunas?city=cali&zone=escogepersona
    path('corregimientos_comunas/', views.corregcomunas_list),
#GET /veredas_neighborhoods?city=cali&zone=escogepersona
    path('veredas_neighborhoods/', views.neighborvereda_list),
#GET /zones
    path('zones/', views.zones_list),
    #4. campanas
    path('activecampaigns/', views.acampaigns_list),
    path('notactivecampaigns/', views.notacampaigns_list), 
    path('roleu/<int:pk>/', views.roleuser_list),
    #path('users', views.users),
#Pagina Campañas
    path('keywords/', views.fivekeywords_list), 
    path('gender_list/', views.gender_list), 
    path('ages/', views.age_range_list), 
    path('comunacorr/', views.create_comunacorr),
    path('population_comunas/', views.population_comunas_list),
    path('educations/', views.education_visualization_list),
    path('saveall/', views.save_info),
    path('register/', views.register),
    path('save_info_zone/', views.save_info_zone),
    path('campaign/', views.save_campaign),
    path('save_info_ruser/', views.save_info_registered_user),
    path('change_zone/', views.t_change_zone),
    #profile
   
    path('acampaigns_person_list/', views.acampaigns_person_list),
    path('person_data/', views.person_data),
    path('campaigns_created_person/', views.campaigns_created_person),
    path('campaigns_person/', views.campaigns_person),
    path('city_person/', views.city_person),
    path('predict/',views.predictTopic),

    #new endpoints
    path('obtain_opendata/', views.obtain_opendata),
    path('obtain_percentage/', views.obtain_percentage),
    path('narratives/', views.narratives_list),
    path('narrative_user_campaign/', views.narratives_campaign_list),
    path('role_user/', views.role_user),
    path('topic_list/', views.topic_list),
    path('topic_person_campaign/', views.topic_person_campaign),
    path('obtain_campaign/', views.obtain_campaign),
    path('create_person/', views.create_person),
    path('obtain_person_campaign_logged/', views.obtain_person_campaign_logged),



    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


