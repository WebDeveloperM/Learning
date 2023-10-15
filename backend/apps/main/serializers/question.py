from rest_framework import serializers
from main.models import Option, Science, Question
from main.serializers.sciences import ScienceSerializer
from main.serializers.option import OptionSerializer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'science', 'level')

    def to_representation(self, instance):
        options = Option.objects.filter(question__id = instance.id)
        ret = super().to_representation(instance)
        ret["option"] = OptionSerializer(options, many=True).data
        return ret