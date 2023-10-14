from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Lesson
from main.serializers.lessons import LessonSerializer


class LessonApiView(APIView):
    permission_classes = (AllowAny,) 

    def get(self, request):
        lessons = Lesson.objects.all()
        return Response(LessonSerializer(lessons, many=True).data)
