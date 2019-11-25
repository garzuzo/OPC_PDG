from django.urls import include, path
from rest_framework import routers
from . import views
#Auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,

)

router = routers.DefaultRouter()
router.register(r'roleusers',views.RoleUserViewSet)
router.register(r'gender', views.GenderViewSet)
router.register(r'levelseducation', views.HigherLevelEducationViewSet)
#router.register(r'states', views.states_list)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   # path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/levelineducation/', views.leveleducation_list),
#GET /api/states?country=colombia
    path('api/states/', views.states_list),
#GET /api/cities?state=escogepersona
    path('api/cities/', views.cities_list),
#GET /api/corregimientos_comunas?city=cali&zone=escogepersona
    path('api/corregimientos_comunas/', views.corregcomunas_list),
#GET /api/veredas_neighborhoods?city=cali&zone=escogepersona
    path('api/veredas_neighborhoods/', views.neighborvereda_list),
#GET /api/zones
    path('api/zones/', views.zones_list),
    #4. campanas
    path('api/activecampaigns/', views.acampaigns_list),
    path('api/notactivecampaigns/', views.notacampaigns_list), 
    path('roleu/<int:pk>/', views.roleuser_list),
    #path('api/users', views.users),
#Pagina Campañas
    path('api/keywords/', views.fivekeywords_list), 
    path('api/women_men/', views.womenmen_campaign_list), 
    path('api/ages/', views.age_range_campaign_list), 
    path('api/comunacorr/', views.create_comunacorr),
    path('api/population_comunas/', views.population_comunas_list),
    path('api/narratives/', views.narratives_campaign_list),
    path('api/educations/', views.education_campaign_list),
    path('api/saveall/', views.save_info),
    path('api/validuser/', views.valid_user),
    path('api/register/', views.register),
    path('api/save_info_zone/', views.save_info_zone),
    path('api/campaign/', views.save_campaign),
    path('api/save_info_ruser/', views.save_info_registered_user),
    path('api/change_zone/', views.t_change_zone),
    #profile
    path('api/person_data/', views.person_data),
    path('api/campaigns_created_person/', views.campaigns_created_person),
    path('api/campaigns_person/', views.campaigns_person),
    path('api/city_person/', views.city_person),
    path('api/predict/',views.predictTopic),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


