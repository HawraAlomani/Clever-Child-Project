from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegisterSerializer


# to create a user account
@api_view(['POST'])
def register_user(request: Request):
    user_serializer = UserRegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()
        data = {
            "msg": "Created user successfully."
        }
        return Response(data)
    else:
        print(user_serializer.errors)
        data = {
            "msg": "Couldn't create user."
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


# to login (access database and authenticate),then authenticated user will be given a token
@api_view(['POST'])
def login_user(request: Request):
    if 'username' in request.data and 'password' in request.data:
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = AccessToken.for_user(user)
            responseData = {
                "msg": "Your token is ready",
                "token": str(token)
            }
            return Response(responseData)
    data = {
        "msg": "Please provide your username and password."
    }
    return Response(data, status=status.HTTP_401_UNAUTHORIZED)
