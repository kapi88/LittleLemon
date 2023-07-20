
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers



urlpatterns = [ 
    path('admin/', admin.site.urls),

    # ---- Restaurant --------
    path('', include('restaurant.urls')),

    #------ API --------
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
