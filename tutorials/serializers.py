import serpy
from rest_framework import serializers

from .models import Tutorial, Result


class ObjectiveSerializer(serpy.Serializer):
    type = serpy.Field()
    case = serpy.Field()


class StepSerializer(serpy.Serializer):
    title = serpy.Field()
    description = serpy.Field()
    objective = ObjectiveSerializer()


class TutorialSerializer(serializers.ModelSerializer):
    complete = serializers.SerializerMethodField()

    class Meta:
        model = Tutorial
        fields = ['id', 'number', 'title', 'step_count', 'complete']

    def get_complete(self, obj):
        request = self.context.get("request")

        if request and hasattr(request, "user"):
            user = request.user

            return Result.objects.filter(user_id=user.id, tutorial_id=obj.id).exists()

        return False


class TutorialDetailSerializer(TutorialSerializer):
    steps = StepSerializer(attr='steps.all', many=True, call=True, required=False)

    class Meta:
        model = Tutorial
        exclude = []
        depth = 2


class TutorialCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        exclude = []


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        exclude = []
