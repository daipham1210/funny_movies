from pydoc import describe
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from movies.models import Movie

from movies.serializers import MovieSerializer
from django.http import HttpResponseRedirect

def index(request):
    list_movies_qs = Movie.objects.all().select_related('user').only('user__email', 'url', 'title', 'description').order_by('-id')[:20]
    list_movies = MovieSerializer(list_movies_qs, many=True).data
    return render(request, "list_movies.html", dict(list_movies=list_movies))

@login_required
def share_movie(request):
    if request.method == "POST":
        data = dict(
            url=request.POST.get("url"),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            user=request.user.id,
        )
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect("/")
    return render(request, "share_form.html")
