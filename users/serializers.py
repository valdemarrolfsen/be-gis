import serpy
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serpy.Serializer):
    id = serpy.IntField()
    username = serpy.StrField()
    email = serpy.StrField()
    first_name = serpy.Field(required=False)
    last_name = serpy.Field(required=False)

    # Status
    is_active = serpy.BoolField()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []

    def create(self, validated_data):
        # Create the auth user
        user = get_user_model().objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user
