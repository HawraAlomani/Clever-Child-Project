from django.contrib import admin
from .models import Course, CourseSubscription, FavoriteCourses

admin.site.register(Course)
admin.site.register(CourseSubscription)
admin.site.register(FavoriteCourses)

