from rest_framework import serializers
from main.models import SpecialOption, Science, SpecialQuestion
from main.serializers.sciences import ScienceSerializer
from main.serializers.sp_option import SpecialOption


class SpQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOption
        fields = ('id', 'text', 'science', 'question_time', 'level')

    def to_representation(self, instance):
        science = Science.objects.filter(science__id=instance.id)
        options = SpecialOption.objects.filter(question__id = instance.id)
        ret = super().to_representation(instance)
        ret["science"] = ScienceSerializer(science, many=True).data
        ret["option"] = SpecialOption(options, many=True).data
        return ret