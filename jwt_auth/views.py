from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

from.serializers import UserProfileSerializer, UserRegistrationSerializer
User = get_user_model()

class UserRegisterView(CreateAPIView):
    ''' View for Users Registration /register POST'''
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class UserLoginView(APIView):
    ''' View for Users Login /login POST'''

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user_to_login = User.objects.get(username=username)
        except User.DoesNotExist:
            raise PermissionDenied({'detail':'Unauthorized'})

        if not user_to_login.check_password(password):
            raise PermissionDenied({'detail':'Unauthorized'})

        expiry_time = datetime.now() + timedelta(days=7)

        token = jwt.encode(
            {'sub': user_to_login.id, 'exp': int(expiry_time.strftime('%s'))},
            settings.SECRET_KEY,
            algorithm='HS256'
        )

        return Response({
            'token': token,
            'message': f'Welcome back {user_to_login.username}'
        })


class UserProfileView(RetrieveAPIView):
    '''View for User Profile'''

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, )