from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Question
from main.serializers.question import QuestionSerializer


class QuestionApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        questions = Question.objects.all()
        return Response(QuestionSerializer(questions, many=True).data)
    
    def post(self, request):
        science_id = request.data.get("science_id")
        print(type(science_id))
        questions = Question.objects.filter(science__id = science_id)
        print(questions)
        return Response(QuestionSerializer(questions, many=True).data)
