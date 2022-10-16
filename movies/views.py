from django.shortcuts import render
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from movies.serializers import MovieSerializer
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def index(request):
    list_movies_qs = Movie.objects.all().select_related('user').only('user__email', 'url', 'title', 'description').order_by('-id')
    paginator = Paginator(list_movies_qs, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "list_movies.html", dict(page_obj=page_obj))

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
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            messages.add_message(request, messages.INFO, "Shared video successfully")
            return HttpResponseRedirect("/")
        else:
            messages.add_message(request, messages.ERROR, "Something error.")
    return render(request, "share_form.html")
