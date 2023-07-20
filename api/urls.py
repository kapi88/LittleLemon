
from django.urls import include, path
from api.views import UserViewSet
from rest_framework import routers
from .views import MenuItemView, SingleMenuItemView, BookingViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tables', BookingViewSet)

urlpatterns = [
    path('', include(router.urls)),#add following lines to urlpatterns list 
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    
    ]