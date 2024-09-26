from django import forms
from django.contrib import admin
from .models import customer_information, dog_information, appointment_information


class AppointmentInformationForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        queryset=customer_information.objects.all(), required=True, label="Dueño"
    )

    class Meta:
        model = appointment_information
        fields = ["owner", "dog", "date", "purpose"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Inicializar queryset de perros vacío
        self.fields["dog"].queryset = dog_information.objects.none()

        if "owner" in self.data:
            try:
                owner_id = int(self.data.get("owner"))
                self.fields["dog"].queryset = dog_information.objects.filter(
                    owner_id=owner_id
                ).order_by("name")
            except (ValueError, TypeError):
                pass  # Invalid input from the client; ignore and fallback to empty Dog queryset
        elif self.instance.pk:
            self.fields["dog"].queryset = self.instance.dog.owner.dogs.all().order_by(
                "name"
            )


class AppointmentInformationAdmin(admin.ModelAdmin):
    form = AppointmentInformationForm

    class Media:
        js = ("js/update_dogs.js",)  # Asegúrate de que el archivo JS esté en esta ruta

    def change_view(self, request, object_id, form_url="", **kwargs):
        response = super().change_view(request, object_id, form_url, **kwargs)
        if response.status_code == 200:
            response.content = response.content.replace(
                b"</head>",
                b"<script>updateDogs();</script></head>",  # Inyecta la función JS
            )
        return response


# Register your models here.
admin.site.register(customer_information)
admin.site.register(dog_information)
admin.site.register(appointment_information, AppointmentInformationAdmin)
