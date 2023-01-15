from .models import User,Todo
from rest_framework import serializers,validators

class UserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    class Meta:
        model=User
        fields=["email"]

class TodoSerializer(serializers.ModelSerializer):
    # created_by = serializers.ReadOnlyField(source='creator.email')
    class Meta:
        model=Todo
        fields=["created_by","title","description","created_at"]