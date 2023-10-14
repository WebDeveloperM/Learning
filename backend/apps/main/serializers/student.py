from rest_framework import serializers
from main.models import Student, Science
from users.models import User
from users.serializers.sign_in import UserSerializer
from main.serializers.sciences import ScienceSerializer


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'group')

    def to_representation(self, instance):
        users = User.objects.filter(id=instance.id)
        science = Science.objects.filter(id=instance.id)
        ret = super().to_representation(instance)
        ret["user"] = UserSerializer(users, many=True).data
        ret["science"] = ScienceSerializer(science, many=True).data
        return ret