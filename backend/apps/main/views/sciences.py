from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Science
from main.serializers.sciences import ScienceSerializer
from rest_framework.permissions import IsAuthenticated


class ScienceApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sciences = Science.objects.all()
        return Response(ScienceSerializer(sciences, many=True).data)
