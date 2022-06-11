from rest_framework import serializers
from .models import Course


# to convert Course Model to JSON
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
