from rest_framework import serializers
from .models import Movie
from user.models import User


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Movie
        fields = ["url", "title", "description", "user", "created_at", "updated_at"]