from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Control
from main.serializers.control import ControlSerializer


class ControlApiView(APIView):

    def get(self, request):
        controls = Control.objects.all()
        return Response(ControlSerializer(controls, many=True).data)
