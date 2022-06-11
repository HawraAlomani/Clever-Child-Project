from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    added_by = models.CharField(max_length=70)

    CHOICES = (
        ("EE", "Electrical Engineering"),
        ("CPE", "Computer Engineering"),
        ("CS", "Computer Science"),
    )

    category = models.CharField(max_length=80, choices=CHOICES)
    video = models.FileField(upload_to="videos/", null=True)
    image = models.ImageField(upload_to="images/", null=True)
    summary = models.TextField(max_length=700)
