from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import User, SmsCode
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from users.models import Token


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
