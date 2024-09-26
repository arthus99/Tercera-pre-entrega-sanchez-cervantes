from django.shortcuts import render, redirect
from django.http import HttpRequest
from django import forms
from .models import customer_information, dog_information


class test123_validation(forms.Form):
    name = forms.CharField(label="Name")


# Create your views here.
def index(request):
    return render(request, "doggyDayCareCustomerInterface/index.html")


def aboutUs(request):
    return render(request, "doggyDayCareCustomerInterface/html/aboutUs.html")


def contactUsPage(request):
    return render(request, "doggyDayCareCustomerInterface/html/contactUsPage.html")


def createNewProfile(request):
    return render(request, "doggyDayCareCustomerInterface/html/createNewProfile.html")


def test123(request):
    return render(
        request,
        "doggyDayCareCustomerInterface/html/test123.html",
        {"form": test123_validation()},
    )


def greetings(request):
    if request.method == "POST":
        form = test123_validation(request.POST)
        if form.is_valid():
            obj = form.cleaned_data["name"]

        return render(
            request, "doggyDayCareCustomerInterface/html/greetings.html", {"form": obj}
        )


class logInPage_validation(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "fieldstyle"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "fieldstyle"})
    )


def logInPage(request):
    return render(
        request,
        "doggyDayCareCustomerInterface/html/login.html",
        {"form": logInPage_validation()},
    )


def customerProfile(request):
    if request.method == "POST":
        form = logInPage_validation(request.POST)
        if form.is_valid():
            obj1 = form.cleaned_data["username"]
            obj2 = form.cleaned_data["password"]
            table_val = customer_information.objects.filter(
                username=obj1, password=obj2
            )

            if table_val.exists():
                row = table_val.first()
                return render(
                    request,
                    "doggyDayCareCustomerInterface/html/customerProfile.html",
                    {"form": row},
                )
            else:
                return redirect("logInPage")
    else:
        form = (
            logInPage_validation()
        )  # Proporcionar un formulario vacío para el método GET

    return render(request, "doggyDayCareCustomerInterface/login.html", {"form": form})
