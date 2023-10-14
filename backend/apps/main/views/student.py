from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from main.models import Student
from main.serializers.student import StudentSerializer


class StudentApiView(APIView):

    def get(self, request):
        students = Student.objects.all()
        return Response(StudentSerializer(students, many=True).data)
