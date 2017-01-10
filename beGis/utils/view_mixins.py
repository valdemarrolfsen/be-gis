from django.http import Http404
from rest_framework.settings import api_settings
from rest_framework.views import APIView


class PaginatedView(APIView):
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        return self._paginator

    def paginate_queryset(self, queryset):
        """
        Return a single page of results, or `None` if pagination is disabled.
        """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        """
        Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class ModelView(PaginatedView):
    """
    A paginated view that defines a get_object method. Checks object permission and raises 404 if not found.
    Method takes **kwargs also, so it is possible to query based on fields other than primary key.
    """
    model = None
    required_groups = None

    def get_object(self, pk, **kwargs):
        try:
            obj = self.model.objects.get(pk=pk, **kwargs)
        except self.model.DoesNotExist:
            raise Http404
        self.check_object_permissions(self.request, obj)
        return obj

    @staticmethod
    def get_error_object(key, error_messages):
        return {
            key: error_messages
        }
