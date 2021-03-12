from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from myopinion.settings import EMAIL_HOST_USER, SECRET_KEY
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
import jwt
from .tasks import send_async_email


# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request) -> Response():
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = serializer.data

        token: object = RefreshToken().for_user(user).access_token  # obtain access token for created user

        relative_link: str = reverse('email-verify')
        current_site: str = get_current_site(request).domain
        absurl = f'http://{current_site}{relative_link}?token={token}'
        email_body = f'{user.username} use this link to verify your account: \n {absurl} '
        data = {
            'subject': 'Verify Email',
            'body': email_body,
            'to': (user.email,),
            'from_email': EMAIL_HOST_USER,
        }

        # Util.send_email(data) # send email with a new thread

        send_async_email.delay(data)  # send email with celery

        return Response(user_data, status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    def get(self, request) -> Response():
        token = request.GET.get('token')

        try:
            payload: dict = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'response': 'Email is verified'}, status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Token expired'}, status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request) -> Response():
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
