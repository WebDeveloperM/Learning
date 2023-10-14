from rest_framework import serializers
from main.models import Science
from users.models import User
from users.serializers.sign_in import UserSerializer



class ScienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Science
        fields = ('id', 'title', 'teacher')

    def to_representation(self, instance):
        users = User.objects.filter(id=instance.id)
        ret = super().to_representation(instance)
        ret["user"] = UserSerializer(users, many=True).data
        return ret