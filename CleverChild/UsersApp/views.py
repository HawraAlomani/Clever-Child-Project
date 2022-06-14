from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import UserRegisterSerializer, ParentSerializer, ChildSerializer, SpecialistSerializer
from .models import *


# to create a user account
@api_view(['POST'])
def register_user(request: Request):
    """
      - A function to register users
      - It checks if it is a normal user, parent, child, or specialist.
      - Creates a user account, and a profile of the specific type.

        :param request:
        :return: a message of the type of registered account, or the status of creating a user.
    """
    user_serializer = UserRegisterSerializer(data=request.data)

    if user_serializer.is_valid():
        new_user = User.objects.create_user(**user_serializer.data)
        new_user.save()

        if 'profile' in request.query_params:
            if request.query_params["profile"] == "parent":
                parentProfile = Parent(user=new_user, birth_date=request.data["birth_date"],
                                       country=request.data["country"],
                                       phone_number=request.data["phone_number"])
                parentProfile.save()
                data = {
                    "msg": "Created a parent account successfully.",

                }
                return Response(data)
            elif request.query_params["profile"] == "child":
                parent_id = request.query_params.get("parent_id", None)
                if parent_id is None:
                    return Response({"msg": "you must provide parent id"})
                childProfile = Child(user=new_user, age=request.data["age"], interest=request.data["interest"],
                                     parent=Parent.objects.get(id=parent_id))
                childProfile.save()
                data = {
                    "msg": "Created a child account successfully."
                }
                return Response(data)
            elif request.query_params["profile"] == "specialist":
                specialistProfile = Specialist(user=new_user, specialization=request.data["specialization"],
                                               degree=request.data["degree"],
                                               graduation_date=request.data["graduation_date"],
                                               country=request.data["country"])
                specialistProfile.save()
                data = {
                    "msg": "Created a specialist account successfully."
                }
                return Response(data)
            else:
                data = {
                    "msg": "Created a general user account successfully."
                }
                return Response(data)
        data = {
            "msg": "Created a general user account successfully."
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
    """
          - A function to login users
          - It checks if username & password in database using authenticate, then provide a token.

            :param request:
            :return: a token is provided if successful.
    """
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
