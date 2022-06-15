from rest_framework import serializers
from .models import Course, CourseSubscription, FavoriteCourses


# to convert Course Model to JSON
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


# to convert course subscriptions Model to JSON
class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = '__all__'


# to convert favorite courses Model to JSON
class FavoriteCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCourses
        fields = '__all__'
