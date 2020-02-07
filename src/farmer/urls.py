from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('landRegister', views.landRegister, name="landRegister"),
    path('land', views.land, name="land"),
    path('profile',views.profile,name="profile"),
    path('search',views.search,name="search")
]
