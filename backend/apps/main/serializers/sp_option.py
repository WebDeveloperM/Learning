from rest_framework import serializers
from main.models import SpecialOption


class SpOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialOption
        fields = ('id', 'text', 'question', 'correct')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return ret