from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request: Request):
    # only authenticated users can add a course.
    # Need to write code for (admin/specialists has permission)
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    new_course = CourseSerializer(data=request.data)
    if new_course.is_valid():
        new_course.save()
        dataResponse = {
            "msg": "The course is added successfully.",
            "course": new_course.data
        }
        return Response(dataResponse)
    else:
        print(new_course.errors)
        dataResponse = {
            "msg": "Couldn't add the course."
        }
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def display_courses(request: Request):
    courses = Course.objects.all()

    dataResponse = {
        "msg": "List of available courses.",
        "courses": CourseSerializer(instance=courses, many=True).data
    }
    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_course(request: Request, course_id):
    # only authenticated users can delete a course.
    # Need to write code for (admin has permission)
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    course = Course.objects.get(id=course_id)
    course.delete()
    data = {
        "msg": "The course is deleted."
    }
    return Response(data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_course(request: Request, course_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    course = Course.objects.get(id=course_id)
    updated_course = CourseSerializer(instance=course, data=request.data)
    if updated_course.is_valid():
        updated_course.save()
        dataResponse = {
            "msg": "The course information is updated."
        }

        return Response(dataResponse)
    else:
        print(updated_course.errors)
        dataResponse = {
            "msg": "Unable to update course information."
        }
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)
