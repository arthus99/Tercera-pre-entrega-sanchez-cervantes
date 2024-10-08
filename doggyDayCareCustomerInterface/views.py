from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, JsonResponse
from django import forms
from .models import customer_information, dog_information, appointment_information
from .forms import CustomerInformationForm, DogInformationForm


def get_dogs(request):
    owner_id = request.GET.get("owner_id")
    dogs = dog_information.objects.filter(owner_id=owner_id).values("id", "name")
    return JsonResponse(list(dogs), safe=False)


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


def insert_customer_succeded(request):
    return render(
        request,
        "doggyDayCareCustomerInterface/html/insert_customer_information_succeeded.html",
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


def insert_customer_information(request):
    if request.method == "POST":
        form = CustomerInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("insert_custumer_succeded")
    else:
        form = CustomerInformationForm()

    return render(
        request,
        "doggyDayCareCustomerInterface/html/insert_customer_information.html",
        {"form": form},
    )


def add_dog(request):
    if request.method == "POST":
        form = DogInformationForm(request.POST)
        if form.is_valid():
            dog_instance = form.save()
            return redirect("success_dog", dog_id=dog_instance.id)
    else:
        form = DogInformationForm()

    return render(
        request, "doggyDayCareCustomerInterface/html/add_dog.html", {"form": form}
    )


def insert_dog_succeded(request, dog_id):
    dog = get_object_or_404(dog_information, id=dog_id)
    return render(
        request, "doggyDayCareCustomerInterface/html/succed_dog.html", {"dog": dog}
    )


def create_appointment(request):
    if request.method == "POST":
        owner_id = request.POST.get("owner")
        dog_id = request.POST.get("dog")
        date = request.POST.get("date")
        purpose = request.POST.get("purpose")

        # Crear una nueva cita
        appointment = appointment_information(dog_id=dog_id, date=date, purpose=purpose)
        appointment.save()  # Guarda la cita en la base de datos

        return redirect("appointment-success")
    # Si es una solicitud GET, obtener todos los propietarios
    owners = customer_information.objects.all()

    context = {
        "owners": owners,
    }
    return render(
        request, "doggyDayCareCustomerInterface/html/create_appointment.html", context
    )


def appointment_success(request):
    return render(
        request,
        "doggyDayCareCustomerInterface/html/appointment-succeeded.html",
    )


def find_dog_form(request):

    return render(request, "doggyDayCareCustomerInterface/html/find_dog.html")


def dog_finder(request):
    dog = request.GET["dog"]

    dogs = dog_information.objects.filter(name__icontains=dog)

    return render(
        request,
        "doggyDayCareCustomerInterface/html/dogFinder_success.html",
        {"dogs": dogs},
    )
