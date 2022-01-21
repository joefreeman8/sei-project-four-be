# from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from.serializers import UserRegistrationSerializer
User = get_user_model()

class UserRegisterView(CreateAPIView):
    ''' View for Users Registration /register POST'''
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer