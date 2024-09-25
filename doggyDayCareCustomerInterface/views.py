from django.shortcuts import render
from django.http import HttpRequest
from django import forms


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
