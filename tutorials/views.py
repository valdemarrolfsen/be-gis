# Rest Framework
from rest_framework import permissions, status
from rest_framework.response import Response

# Utils
from beGis.utils.view_mixins import ModelView, PaginatedView

# Local
from .models import Tutorial, Step, Objective, Result
from .serializers import TutorialSerializer, TutorialDetailSerializer, TutorialCreateSerializer, ResultSerializer


class TutorialListCreateView(PaginatedView):
    permission_classes = [permissions.IsAuthenticated, ]
    model = Tutorial

    def get(self, request):
        tutorials = Tutorial.objects.all()

        page = self.paginate_queryset(tutorials)

        if page is not None:
            serializer = TutorialSerializer(page, many=True, context={'request': request})

            return self.get_paginated_response(serializer.data)

        data = TutorialSerializer(tutorials, many=True, context={'request': request}).data
        return Response(data=data)


class TutorialDetailView(ModelView):
    permission_classes = [permissions.IsAuthenticated, ]
    model = Tutorial

    def get(self, request, pk):
        tutorial = self.get_object(pk)
        data = TutorialDetailSerializer(tutorial, context={'request': request}).data

        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tutorial = self.get_object(pk=pk)
        serializer = TutorialCreateSerializer(instance=tutorial, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ResultListCreateView(ModelView):
    permission_classes = [permissions.IsAuthenticated, ]
    model = Result

    def post(self, request, tutorial_pk):
        serializer = ResultSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
