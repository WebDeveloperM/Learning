from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from main.models import Answer, Question, Option, Student
from main.serializers.answer import AnswerSerializer
from main.serializers.question import QuestionSerializer
import datetime
from django.db.models import Q


class AnswerApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        answers = Answer.objects.all()
        return Response(AnswerSerializer(answers, many=True).data)
    
    def post(self, request):
        all_answers = []
        answer_arr = request.data
        for answer_obj in answer_arr:
            student_id = answer_obj['student_id']
            question_id = answer_obj['question_id']
            option_id = answer_obj['option_id']
        
            _question = Question.objects.filter(id = question_id).first()
            _student = Student.objects.filter(id=student_id).first()
            _option = Option.objects.filter(id=option_id).first()
            _right_option = Option.objects.filter(Q(question__id = question_id) & Q(correct = True) ).first()
            
            if _option.correct == _right_option.correct:
                right_answer = Answer.objects.create(
                    student=_student,
                    question= _question,
                    option = _option,
                    correct = True,
                    response_time = datetime.datetime.now(),
                    )
                
                data = {"student": _student.id,
                        "quesion_id": question_id,
                        "result" : True
                        }
                all_answers.append(data)
            else:
                err_answer = Answer.objects.create(
                    student=_student,
                    question= _question,
                    option = _option,
                    correct = False,
                    response_time = datetime.datetime.now(),
                    )
                data = {"student": _student.id,
                              "quesion_id": question_id,
                              "result" : False
                              }
                all_answers.append(data)
        return Response(all_answers, 200)
