from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import User, SmsCode
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from users.serializers.sign_in import UserSerializer
from users.utils.send_code import send_code


class SignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        phone = request.data.get('phone')
        email = request.data.get('email')
        password = request.data.get('password')
        type = request.data.get('type')

        if len(phone) != 13:
            raise ParseError('This phone number is incorrect!', 400)

        res = send_code(request.data['phone'])
        user, created = User.objects.update_or_create(
            phone=phone,
            defaults={
                'email': email,
                'password': password,
                'username': phone,
                'type': type,
                'dispatch_id': res['dispatch_id']
            }
        )
       
        serializer = UserSerializer(user).data

        return Response(serializer, 201)

