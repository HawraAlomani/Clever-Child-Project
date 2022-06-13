from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from UsersApp.models import Child


# model for courses
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
    video = models.URLField()
    image = models.URLField()
    summary = models.TextField(max_length=700)

    def __str__(self):
        return self.title


# model for course subscriptions
class CourseSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])


# model for favorite courses
class FavoriteCourses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
