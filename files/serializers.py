import serpy
from rest_framework import serializers

from .models import File


class FileSerializer(serpy.Serializer):
    owner = serpy.Field()
    file = serpy.Field()

class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        exclude = []
