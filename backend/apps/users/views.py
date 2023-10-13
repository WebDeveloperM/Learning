from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import User, SmsCode
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from users.serializers import UserSerializer
from users.utils.send_code import send_code


class SignInView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        phone = request.data.get('phone')
        type = request.data.get('type')
        region = request.data.get('region')

        if len(phone) != 13:
            raise ParseError('This phone number is incorrect!', 400)

        res = send_code(request.data['phone'])
        user, created = User.objects.update_or_create(
            phone=phone,
            defaults={
                'email': phone,
                'username': phone,
                'type': type,
                'region': region,
                'dispatch_id': res['dispatch_id']
            }
        )
       
        serializer = UserSerializer(user).data

        return Response(serializer, 201)


class VerificationView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        dispatch_id = request.data.get('dispatch_id')
        code = request.data.get('code')
        user = User.objects.filter(dispatch_id=dispatch_id).first()
        sms_code = SmsCode.objects.filter(dispatch_id=dispatch_id).first()

        if not sms_code or sms_code.code != code:
            raise ParseError('Verification code incorrect. Try again.', 400)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, 201)
