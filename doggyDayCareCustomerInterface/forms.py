from django import forms
from .models import customer_information, dog_information, appointment_information


class CustomerInformationForm(forms.ModelForm):
    class Meta:
        model = customer_information
        fields = [
            "username",
            "password",
            "firstName",
            "lastName",
            "gender",
            "address",
            "state",
        ]
        widgets = {
            "password": forms.PasswordInput(),
        }


class DogInformationForm(forms.ModelForm):
    class Meta:
        model = dog_information
        fields = ["owner", "name", "age"]

    owner = forms.ModelChoiceField(
        queryset=customer_information.objects.all(), label="Owner"
    )
    name = forms.CharField(max_length=64, label="Dog's name")
    age = forms.IntegerField(min_value=0, label="Age (in years))")
