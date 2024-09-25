from django.db import models


# Create your models here.
class customer_information(models.Model):
    customer_id = models.IntegerField()  # (primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=20)
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=64)
    state = models.CharField(max_length=64)


class dog_information(models.Model):
    dog_id = models.ForeignKey(customer_information, on_delete=models.CASCADE)
    dog_name1 = models.CharField(max_length=64)
    dog_name2 = models.CharField(max_length=64)
    dog_age1 = models.IntegerField()
    dog_age2 = models.IntegerField()
