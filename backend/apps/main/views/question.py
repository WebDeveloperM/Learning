from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Question
from main.serializers.question import QuestionSerializer


class QuestionApiView(APIView):

    def get(self, request):
        questions = Question.objects.all()
        return Response(QuestionSerializer(questions, many=True).data)
