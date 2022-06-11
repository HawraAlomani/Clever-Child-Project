from django.urls import path
from . import views

app_name = "course"
# CRUD API endpoints for course
urlpatterns = [
    path("add/", views.add_course, name="add_course"),
    path("display_courses/", views.display_courses, name="display_courses"),
    path("update/<course_id>", views.update_course, name="update_course"),
    path("delete/<course_id>", views.delete_course, name="delete_course")
]