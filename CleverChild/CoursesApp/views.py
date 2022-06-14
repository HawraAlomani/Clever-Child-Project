from rest_framework.decorators import api_view, authentication_classes
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Course, CourseSubscription
from .serializers import CourseSerializer, CourseSubscriptionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# CRUD on Courses: Add, Display, Delete, Update.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_course(request: Request):
    """
- A function to add courses.
- It checks for authentication (whether the user is logged in or not).
- Only users who have permission can add a course.
- Admin and Specialists have permission.

    :param request:
    :return: message of the status of operation, or the added course data.
    """
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed."}, status=status.HTTP_401_UNAUTHORIZED)
    if not request.user.has_perm('CoursesApp.add_course'):
        return Response({"msg": "Not Allowed, you don't have permission."}, status=status.HTTP_401_UNAUTHORIZED)
    request.data["user"] = request.user.id
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
    """
 - A function to display all courses.
 - No permission or authentication is needed.

     :param request:
     :return: list of courses with course details.
     """
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
    """
    - A function to delete courses.
    - It checks for authentication (whether the user is logged in or not).
    - Only users who have permission can delete a course.
    - Admin and Specialists have permission.

        :param course_id:
        :param request:
        :return: message of the status of operation, or if the course is deleted.
    """

    # only authenticated users can delete a course.
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if not request.user.has_perm('CoursesApp.delete_course'):
        return Response({"msg": "Not Allowed, you don't have permission."}, status=status.HTTP_401_UNAUTHORIZED)
    request.data["user"] = request.user.id
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
    """
    - A function to update course information.
    - It checks for authentication (whether the user is logged in or not).
    - Only users who have permission can update a course.
    - Admin and Specialists have permission.

        :param course_id:
        :param request:
        :return: message of the status of operation, or a message that the course is updated.
    """
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


# CRUD on Course Subscriptions: subscribe, unsubscribe, edit subscription, view all subscriptions.

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def subscribe(request: Request, sub_id):
    """
        - A function to subscribe to a course.
        - It checks for authentication (whether the user is logged in or not).
        - Only users who have permission can subscribe to a course.
        - Admin and Parent have permission.

            :param sub_id:
            :param request:
            :return: message of the status of operation, or the course is subscribed with its information.
    """
    # only authenticated users can subscribe.
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if not request.user.has_perm('CoursesApp.add_coursesubscription'):
        return Response({"msg": "Not Allowed, you don't have permission."}, status=status.HTTP_401_UNAUTHORIZED)
    # if the course id is in courses list, then it can be added to subscribe list.
    course = Course.objects.filter(id=sub_id)
    if course.exists():
        request.data["user"] = request.user.id
        new_sub = CourseSubscriptionSerializer(data=request.data)
        if new_sub.is_valid():
            new_sub.save()
            data = {
                "msg": "The course is subscribed successfully.",
                "course subscribed": new_sub.data
            }
            return Response(data)
        else:
            print(new_sub.errors)
            dataResponse = {
                "msg": "Couldn't subscribe the course."
            }
            return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg": "The course is subscribed."})


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def unsubscribe(request: Request, sub_id):
    """
           - A function to unsubscribe to a course.
           - It checks for authentication (whether the user is logged in or not).
           - Only users who have permission can unsubscribe to a course.
           - Admin and Parent have permission.

               :param sub_id:
               :param request:
               :return: message of the status of operation, or a message that the course is unsubscribed.
    """
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    if not request.user.has_perm('CoursesApp.delete_coursesubscription'):
        return Response({"msg": "Not Allowed, you don't have permission."}, status=status.HTTP_401_UNAUTHORIZED)
    request.data["user"] = request.user.id
    course_sub = CourseSubscription.objects.get(id=sub_id)
    course_sub.delete()
    data = {
        "msg": "The course is unsubscribed."
    }
    return Response(data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_all_subscriptions(request: Request):
    """
           - A function to view all subscribed courses.
           - It checks for authentication (whether the user is logged in or not).
           - Only users who have permission can view subscribed courses.
           - Admin, Parent, and Child have permission.

               :param request:
               :return: all subscribed courses and their information.
    """
    sub_courses = CourseSubscription.objects.all()

    dataResponse = {
        "msg": "All your courses subscriptions.",
        "subscribed courses": CourseSubscriptionSerializer(instance=sub_courses, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def edit_subscription(request: Request, sub_id):
    """
        - A function to edit subscribed courses (progress).
        - It checks for authentication (whether the user is logged in or not).
        - Only users who have permission can edit subscribed courses (progress).
        - Admin, Parent, and Child have permission.

            :param sub_id:
            :param request:
            :return: updated subscribed courses information such as progress.
    """
    pass
