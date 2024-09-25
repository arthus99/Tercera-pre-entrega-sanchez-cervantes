from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("logInPage", views.logInPage, name="logInPage"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("contactUs", views.contactUsPage, name="contactUs"),
    path("NewProfile", views.createNewProfile, name="newProfile"),
    path("test", views.test123, name="test"),
    path("greetings", views.greetings, name="greetings"),
]
