from rest_framework import serializers
from main.models import SpecialAnswer, SpecialQuestion
from main.serializers.sp_option import SpOptionSerializer
from main.serializers.sp_question import SpQuestionSerializer


class SpAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model =SpecialAnswer
        fields = ('id', 'student', 'question', 'option','correct', 'response_time', 'time_delta' )


    def to_representation(self, instance):
        question = SpecialQuestion.objects.filter(id=instance.id)
        option = SpecialQuestion.objects.filter(id=instance.id)

        ret = super().to_representation(instance)
        ret["question"] = SpQuestionSerializer(question, many=True).data
        ret["option"] = SpOptionSerializer(option, many=True).data
        return ret
    
    