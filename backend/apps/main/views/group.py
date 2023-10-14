from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Group
from main.serializers.group import GroupSerializer


class GroupApiView(APIView):

    def get(self, request):
        groups = Group.objects.all()
        return Response(GroupSerializer(groups, many=True).data)
