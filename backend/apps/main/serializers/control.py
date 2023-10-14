from rest_framework import serializers
from main.models import Control, Science, Student
from main.serializers.student import StudentSerializer
from main.serializers.sciences import ScienceSerializer



class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model =Control
        fields = ('id', 'student', 'control')

    def to_representation(self, instance):
        student = Student.objects.filter(id=instance.id)
        science = Science.objects.filter(id=instance.id)
        ret = super().to_representation(instance)
        ret["student"] = StudentSerializer(student, many=True).data
        ret["science"] = ScienceSerializer(science, many=True).data
        return ret