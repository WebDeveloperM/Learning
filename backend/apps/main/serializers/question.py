from rest_framework import serializers
from main.models import Option, Science, Question
from main.serializers.sciences import ScienceSerializer
from main.serializers.option import OptionSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'science')

    def to_representation(self, instance):
        science = Science.objects.filter(science__id=instance.id)
        options = Option.objects.filter(question__id = instance.id)
        ret = super().to_representation(instance)
        ret["science"] = ScienceSerializer(science, many=True).data
        ret["option"] = OptionSerializer(options, many=True).data
        return ret