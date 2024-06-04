from django.urls import path
from cores import views


urlpatterns = [
    path('', views.index, name="home"),
]

