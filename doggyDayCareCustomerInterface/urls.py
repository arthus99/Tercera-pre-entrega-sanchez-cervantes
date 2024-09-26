from django.urls import path
from . import views
from .views import get_dogs, insert_customer_information

urlpatterns = [
    path("api/get_dogs/", get_dogs, name="get_dogs"),
    path("", views.index, name="index"),
    path("logInPage", views.logInPage, name="logInPage"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("contactUs", views.contactUsPage, name="contactUs"),
    path("NewProfile", views.createNewProfile, name="newProfile"),
    path("test", views.test123, name="test"),
    path("greetings", views.greetings, name="greetings"),
    path("customer", views.customerProfile, name="customer"),
    path("insert_customer", views.insert_customer_information, name="insert_custumer"),
    path(
        "insert_customer_succeeded",
        views.insert_customer_succeded,
        name="insert_custumer_succeded",
    ),
]
