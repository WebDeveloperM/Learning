from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from main.models import Answer
from main.serializers.answer import AnswerSerializer


class AnswerApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        print(request.data)
        answers = Answer.objects.all()
        return Response(AnswerSerializer(answers, many=True).data)
 