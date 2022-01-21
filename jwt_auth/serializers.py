from rest_framework import serializers
from django.contrib.auth import get_user_model
import django.contrib.auth.password_validation as validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from dogs.models import Dog, Favorite, Question

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.pop('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({'detail':'Password and Confirmation do not match'})

        try:
            validation.validate_password(password=password)
        except ValidationError as err:
            raise ValidationError({'password': err})

        attrs['password'] = make_password(password)

        return attrs

    class Meta:
        model = User
        fields = '__all__'

class NestedDogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dog
        fields = '__all__'

class NestedFavoritesSerializer(serializers.ModelSerializer):
    dog = NestedDogSerializer()

    class Meta:
        model = Favorite
        fields = '__all__'

class NestedQuestionSerializer(serializers.ModelSerializer):
    dog = NestedDogSerializer()

    class Meta:
        model = Question
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):

    favorited_dogs = NestedFavoritesSerializer(many=True)
    questions_posted = NestedQuestionSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'favorited_dogs', 'questions_posted')
