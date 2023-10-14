from rest_framework import serializers
from main.models import Control, Option, Answer, Question
from main.serializers.control import ControlSerializer
from main.serializers.option import OptionSerializer
from main.serializers.question import QuestionSerializer



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Answer
        fields = ('id', 'question', 'option', 'correct')

    def to_representation(self, instance):
        control = Control.objects.filter(id=instance.id)
        question = Question.objects.filter(id=instance.id)
        option = Option.objects.filter(id=instance.id)

        ret = super().to_representation(instance)
        ret["control"] = ControlSerializer(control, many=True).data
        ret["question"] = QuestionSerializer(question, many=True).data
        ret["option"] = OptioneSerializer(option, many=True).data
        return ret
    
    