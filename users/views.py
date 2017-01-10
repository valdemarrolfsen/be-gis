from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer, UserCreateSerializer


# Create your views here.

class UserListCreate(APIView):
    """
    Create user view
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, ])
def get_current_user(request):
    """
    Returns the logged in user instance
    """
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)
