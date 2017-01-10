from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from rest_framework.response import Response

from .serializers import FileCreateSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, ])
def file_upload(request):
    """
    """
    serializer = FileCreateSerializer(data=request.data, many=False)
    serializer.is_valid(raise_exception=True)
    serializer.save(owner=request.user)

    return Response(serializer.data, status=status.HTTP_201_CREATED)
