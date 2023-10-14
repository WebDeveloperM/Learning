from rest_framework import serializers
from main.models import Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ('id', 'text', 'question', 'correct')

    def to_representation(self, instance):
    
        ret = super().to_representation(instance)
        return ret