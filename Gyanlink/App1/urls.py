# from django.contrib import admin
from django.urls import path, include
from .views import * 

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('App1.urls')),
    path('', home, name="home"),
    path('stusave/', stusave, name="stusave")
]
