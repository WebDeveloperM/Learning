from rest_framework import serializers
from main.models import Option, Question
from main.serializers.question import QuestionSerializer



class OptioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'text', 'question', 'correct')

    def to_representation(self, instance):
        question = Question.objects.filter(id=instance.id)
        ret = super().to_representation(instance)
        ret["question"] = QuestionSerializer(question, many=True).data
        return ret