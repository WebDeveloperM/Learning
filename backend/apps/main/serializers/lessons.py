from rest_framework import serializers
from main.models import Science, Lesson
from main.serializers.sciences  import ScienceSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'science', 'started_date', 'finished_date')


    def to_representation(self, instance):
        science = Science.objects.filter(id=instance.id)
        ret = super().to_representation(instance)
        ret["science"] = ScienceSerializer(science, many=True).data
        return ret