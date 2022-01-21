from pickletools import read_floatnl
from rest_framework import serializers
from .models import Dog, Favorite, Question
from django.contrib.auth import get_user_model

User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

class QuestionSerializer(serializers.ModelSerializer):
    '''Serializer for Questions'''

    class Meta:
        model = Question
        fields = '__all__'

class NestedQuestionSerializer(serializers.ModelSerializer):
    '''Serializer for nested Questions'''
    owner = NestedUserSerializer()

    class Meta:
        model = Question
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    '''Serializer for the favorites'''

    class Meta:
        model = Favorite
        fields = '__all__'

class NestedFavoriteSerializer(serializers.ModelSerializer): 
    '''Serializer for favorites inside other data'''

    owner = NestedUserSerializer()

    class Meta: 
        model = Favorite
        fields = '__all__'

class DogSerializer(serializers.ModelSerializer):
    '''Serializer for Dogs'''

    favorited_by = NestedFavoriteSerializer(many=True, read_only=True)
    questions = NestedQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Dog
        fields = '__all__'
