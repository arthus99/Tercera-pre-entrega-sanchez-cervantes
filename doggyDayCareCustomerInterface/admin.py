from django.contrib import admin
from .models import customer_information, dog_information

# Register your models here.
admin.site.register(customer_information)
admin.site.register(dog_information)
