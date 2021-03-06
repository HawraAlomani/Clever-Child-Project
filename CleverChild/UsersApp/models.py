from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# customized model for users of type parent
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    # to show list of countries (pip install django-countries)
    country = CountryField(blank=True)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


# customized model for users of type child
class Child(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    interest = models.TextField()
    parent = models.ForeignKey(Parent, related_name="children", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# customized model for users of type specialist
class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=30, help_text="your study area.")
    degree_type = (
        ("1", "Diploma"),
        ("2", "Bachelor"),
        ("3", "Master"),
        ("4", "Doctoral"),
    )
    degree = models.CharField(max_length=80, choices=degree_type)
    graduation_date = models.DateField()
    country = CountryField(blank=True)

    def __str__(self):
        return self.user.username
