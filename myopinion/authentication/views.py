from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from .serializers import RegisterSerializer


# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request) -> Response():
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = serializer.data

        token = RefreshToken().for_user(user).access_token  # obtain access token for created user

        relative_link = reverse('email-verify')
        current_site = get_current_site(request).domain
        absurl = f'http://{current_site}{relative_link}?token={token}'
        email_body = f'{user.username} use this link to verify your account: \n {absurl} '
        data = {
            'subject': 'Verify Email',
            'body': email_body,
            'to': (user.email,),
        }

        Util.send_email(data)

        return Response(user_data, status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        pass
