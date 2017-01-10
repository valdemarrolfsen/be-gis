from django.conf.urls import url

from .views import generate_buffer, generate_diff, generate_intersection, generate_union

urlpatterns = [

    # Tutorials

    url(r'^buffer/$',
        generate_buffer,
        name='generate-buffer'),

    url(r'^difference/$',
        generate_diff,
        name='generate-difference'),

    url(r'^intersection/$',
        generate_intersection,
        name='generate-intersection'),

    url(r'^union/$',
        generate_union,
        name='generate-union')

]
