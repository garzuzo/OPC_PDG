from django.urls import include, path
from rest_framework import routers
from . import views

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
    path('api/veredas_neighborhoods/', views.neigdhborvereda_list),
#GET /api/zones
    path('api/zones/', views.zones_list),
    #4. campanas
    path('api/activecampaigns/', views.acampaigns_list),
    path('api/notactivecampaigns/', views.notacampaigns_list), 
    path('roleu/<int:pk>/', views.roleuser_list),
    #path('api/users', views.users),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


