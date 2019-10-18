from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'roleusers',views.RoleUserViewSet)
router.register(r'gender', views.GenderViewSet)
router.register(r'levelseducation', views.HigherLevelEducationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   # path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api/levelineducation/', views.leveleducation_list),
    path('roleu/<int:pk>/', views.roleuser_list),
    #path('api/users', views.users),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


