from django.urls import path

from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
    path("murtaza", views.murtaza, name="murtaza") 
]
