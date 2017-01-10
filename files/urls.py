from django.conf.urls import url

from .views import file_upload

urlpatterns = [

    # Files
    url(r'^$',
        file_upload,
        name='file-upload'),

]
