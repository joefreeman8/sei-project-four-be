from rest_framework import serializers
from .models import Dog

class DogSerializer(serializers.ModelSerializer):
    '''Serializer for Dogs'''

    class Meta:
        model = Dog
        fields = '__all__'