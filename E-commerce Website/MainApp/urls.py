from django.urls import path
from . import views


app_name = 'MainApp'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
    path('', views.main, name='main'),
]
