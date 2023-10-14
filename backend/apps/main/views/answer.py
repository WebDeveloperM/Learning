from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from main.models import Answer, Question, Option, Student
from main.serializers.answer import AnswerSerializer
import datetime


class AnswerApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        
        answers = Answer.objects.all()
        return Response(AnswerSerializer(answers, many=True).data)
    
    def post(self, request):
        print(request.data)
        answer_arr = request.data
        for answer_obj in answer_arr:
            student_id = answer_obj['student_id']
            question_id = answer_obj['question_id']
            option_id = answer_obj['option_id']

          

            question = Question.objects.filter(id = question_id).first()
            student = Student.objects.filter(id=student_id).first()
            option = Option.objects.filter(id=option_id).first()
            right_option = Option.objects.filter(question__id = question_id).first()
        

            print(question)
            print(student)
            print(option)
            print(right_option)

            if option.correct == right_option.correct:
                answer, created = Answer.objects.update_or_create(
                    student=student,
                    defaults={
                        'question': question,
                        'option': option,
                        'correct': True,
                        'response_time': datetime.datetime.now(),
                    })
                return Response(AnswerSerializer(answer, many=True).data)
            else:
                answer, created = Answer.objects.update_or_create(
                    student=student,
                    defaults={
                        'question': question,
                        'option': option,
                        'correct': False,
                        'response_time': datetime.datetime.now(),
                    })
                return Response(AnswerSerializer(answer, many=True).data)
        
      
        answer, created = Answer.objects.update_or_create(
        student=student,
        defaults={
            'question': question,
            'option': answer,
            'correct': True,
            'response_time': datetime.datetime.now(),
        })
        return Response(AnswerSerializer(answer, many=True).data)
        
 
 