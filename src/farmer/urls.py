from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('landRegister', views.landRegister, name="landRegister"),
    path('land', views.land, name="land"),
    path('profile',views.profile,name="profile"),
    path('search',views.search,name="search")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
