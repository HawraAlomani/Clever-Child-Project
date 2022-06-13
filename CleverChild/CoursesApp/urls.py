from django.urls import path
from . import views

app_name = "course"

urlpatterns = [
    # urls for API endpoints for course
    path("add/", views.add_course, name="add_course"),
    path("display_courses/", views.display_courses, name="display_courses"),
    path("update/<course_id>", views.update_course, name="update_course"),
    path("delete/<course_id>", views.delete_course, name="delete_course"),
    # urls for API endpoints for course subscriptions
    path("subscribe/<title>", views.subscribe, name="subscribe"),
    path("display_subscriptions/", views.view_all_subscriptions, name="display_subscriptions"),
    path("edit_subscription/<sub_id>", views.edit_subscription, name="edit_subscription"),
    path("unsubscribe/<sub_id>", views.unsubscribe, name="unsubscribe")

]
