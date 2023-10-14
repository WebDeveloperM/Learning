from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Option
from main.serializers.option import OptioneSerializer


class OptionApiView(APIView):

    def get(self, request):
        options = Option.objects.all()
        return Response(OptioneSerializer(options, many=True).data)
