from rest_framework import serializers
from .models import Movie
from user.models import User
from urllib.parse import urlparse, parse_qs


class MovieSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = Movie
        fields = ["url", "title", "description", "user", "created_at", "updated_at"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update(
            shared_by_email=instance.user.email,
            iframe=self.__generate_iframe(instance.url)
        )
        return data

    def __get_video_id(self, url):
        """
        Get video id from Youtube Link
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        return: SA2iWivDJiE
        """
        if url:
            query = urlparse(url)
            if query.hostname == 'youtu.be':
                return query.path[1:]
            if query.hostname in ('www.youtube.com', 'youtube.com'):
                if query.path == '/watch':
                    p = parse_qs(query.query)
                    return p['v'][0]
                if query.path[:7] == '/embed/':
                    return query.path.split('/')[2]
                if query.path[:3] == '/v/':
                    return query.path.split('/')[2]
        # fail?
        return None

    def __generate_iframe(self, url):
        video_id = self.__get_video_id(url)
        if video_id:
            return '<iframe width="560" height="315" src="//www.youtube.com/embed/' + video_id + '" frameborder="0" allowfullscreen></iframe>'
        return ""