from django.urls import path, include
from rest_framework import routers
from . import views

r2 = routers.DefaultRouter()
r3 = routers.DefaultRouter()

r2.register('', views.Profile_List)
r3.register('', views.User_List)


urlpatterns = [
    path('profileJS/', include(r2.urls)),
    path('userJS/', include(r3.urls)),
]
