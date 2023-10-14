from rest_framework import serializers
from main.models import Question, Science
from main.serializers.sciences import ScienceSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'science')

    def to_representation(self, instance):
        science = Science.objects.filter(id=instance.id)
        ret = super().to_representation(instance)
        ret["science"] = ScienceSerializer(science, many=True).data
        return ret