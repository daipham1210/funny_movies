from rest_framework import serializers

from movies.services import MovieService
from .models import Movie
from user.models import User


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Movie
        fields = ["url", "title", "description", "user", "created_at", "updated_at"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(
            shared_by_email=instance.user.email,
            iframe=MovieService.generate_iframe_ytb(instance.url)
        )
        return data