from django.db import models


class Flats(models.Model):
    adress = models.CharField(max_length=30)
    postcode = models.CharField(max_length=30)


class Residents(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    NIN = models.CharField(max_length=15, unique=True)
    flat = models.ForeignKey(Flats, on_delete=models.CASCADE)


class Payments(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    resident = models.ForeignKey(Residents, on_delete=models.CASCADE)
# Create your models here.
