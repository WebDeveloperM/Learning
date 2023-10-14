from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Answer
from main.serializers.student import StudentSerializer


class AnswerApiView(APIView):

    def get(self, request):
        answers = Answer.objects.all()
        return Response(StudentSerializer(answers, many=True).data)
