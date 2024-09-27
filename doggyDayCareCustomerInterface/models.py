from django.db import models


# Create your models here.
class customer_information(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    GENDER_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class dog_information(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(
        customer_information, on_delete=models.CASCADE, related_name="dogs"
    )
    name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.owner} :{self.name} ({self.age} years old)"

    class Meta:
        verbose_name_plural = "Dog Information"


class appointment_information(models.Model):
    dog = models.ForeignKey(dog_information, on_delete=models.CASCADE)
    date = models.DateField()
    purpose = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.dog.name} - {self.date} - {self.purpose}"
