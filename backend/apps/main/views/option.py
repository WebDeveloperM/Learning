from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Option
from main.serializers.option import OptionSerializer


class OptionApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        options = Option.objects.all()
        return Response(OptionSerializer(options, many=True).data)
