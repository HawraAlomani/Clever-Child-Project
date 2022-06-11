from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField

# Q: Can I use model User instead of AbstractUser ?

# three type of users: parent,child,specialist.
class User(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_child = models.BooleanField(default=False)
    is_specialist = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# customized model for users of type parent
class Parent(models.Model):
    user = models.OneToOneField(User, related_name="parent")
    birth_date = models.DateField()
    # to show list of countries (pip install django-countries)
    country = CountryField(blank=True)
    phone_number = models.CharField(max_length=10)


# customized model for users of type child
class Child(models.Model):
    user = models.OneToOneField(User, related_name="child")
    age = models.IntegerField()
    interest = models.TextField()
    parent = models.ForeignKey(Parent)


# customized model for users of type specialist
class Specialist(models.Model):
    user = models.OneToOneField(User, related_name="specialist")
    specialization = models.CharField(help_text="your study area.")
    degree_type = (
        ("1", "Diploma"),
        ("2", "Bachelor"),
        ("3", "Master"),
        ("4", "Doctoral"),
    )
    degree = models.CharField(max_length=80, choices=degree_type)
    graduation_date = models.DateField()
    country = CountryField(blank=True)

