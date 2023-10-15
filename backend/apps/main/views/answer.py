from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from main.models import Answer, Question, Option, Student
from main.serializers.answer import AnswerSerializer
from main.serializers.question import QuestionSerializer
import datetime
from django.db.models import Q
from main.models import EASY, MEDIUM, HARD


class AnswerApiView(APIView):
    permission_classes = (AllowAny,) 

    
    
    def post(self, request, id):
        student_id = request.data['student_id']
        question_id = request.data['question_id']
        option_id = request.data['option_id']

        _question = Question.objects.filter(id = question_id).first()
        _student = Student.objects.filter(id=student_id).first()
        _option = Option.objects.filter(id=option_id).first()
        _right_option = Option.objects.filter(Q(question__id = question_id) & Q(correct = True) ).first()

        questions = Question.objects.all()
        id_arr = []
        for q in questions:
            id_arr.append(q.id)

        if _option.correct == _right_option.correct:
            Answer.objects.create(
                    student=_student,
                    question= _question,
                    option = _option,
                    correct = True,
                    response_time = datetime.datetime.now(),
            )

            if _question.level == EASY:
                question = Question.objects.filter(level = MEDIUM)[id]
                serializer = QuestionSerializer(question)
                return Response(serializer.data, 200)
        
            if _question.level == MEDIUM:
                question = Question.objects.filter(level = HARD)[id]
                serializer = QuestionSerializer(question)
                return Response(serializer.data, 200)
        else:
            Answer.objects.create(
                    student=_student,
                    question= _question,
                    option = _option,
                    correct = False,
                    response_time = datetime.datetime.now(),
                )
            
            if _question.level == EASY:
                question = Question.objects.filter(level = EASY)
                serializer = QuestionSerializer(question, many=True)
                return Response(serializer.data, 200)
            
            if _question.level == MEDIUM:
                question = Question.objects.filter(level = EASY)[id]
                serializer = QuestionSerializer(question)
                return Response(serializer.data, 200)
            
            if _question.level == HARD:
                question = Question.objects.filter(level = MEDIUM)[id]
                serializer = QuestionSerializer(question)
                return Response(serializer.data, 200)
         
            
            
class ResultsApiView(APIView):
    permission_classes = (AllowAny,) 
    def get(self, request):
        student_id = request.data.get("student_id")   
        sciensce_id = request.data.get("sciensce_id")   
        answers = Answer.objects.filter(Q(student = student_id) & Q(question__science__id = sciensce_id))
        
        return Response(AnswerSerializer(answers, many=True).data, 200)
