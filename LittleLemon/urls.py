
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [ 
    path('admin/', admin.site.urls),

    # ---- Restaurant --------
    path('', include('restaurant.urls')),

    #------ API --------
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', include_docs_urls(title='LittleLemon API Documentation')),
    #add following lines to update urlpatterns list
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token)
]
