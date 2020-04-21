from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('getApiKey/', views.getApiKey, name='getApiKey'),
    path('setName/', views.setName, name='setName'),
    path('setId/', views.setId, name='setId'),
    path('getObjectInfo/', views.getObjectInfo, name='getObjectInfo'),
]
