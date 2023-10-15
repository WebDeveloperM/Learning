from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Question
from main.serializers.question import QuestionSerializer
from main.models import EASY, MEDIUM, HARD
from django.db.models import Q


class QuestionApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        questions = Question.objects.all()
        id_arr = []
        for q in questions:
            id_arr.append(q.id)
        return Response({"ids": id_arr[:10]}, 200)
    
    def post(self, request):
        science_id = request.data.get("science_id")
        print(type(science_id))
        question = Question.objects.filter(Q(science__id = science_id) & Q(level = EASY )).first()
        print(question)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
