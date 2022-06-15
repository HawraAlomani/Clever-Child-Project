from rest_framework import serializers
from django.contrib.auth.models import User
from UsersApp.models import Parent, Child, Specialist


# serializer to convert user model to JSON
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# serializer to convert parent model to JSON
class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'


# serializer to convert child model to JSON
class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


# serializer to convert specialist model to JSON
class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'
