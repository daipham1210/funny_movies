import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse

UserModel = get_user_model()

# Create your views here.
class LoginOrSignup(LoginView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user and user.is_active:
                login(request, user)
                return JsonResponse(dict(success=True), safe=False, status=200)
            else:
                # Tries to create a new user and add them to the database
                try:
                    user = UserModel.objects.create_user(email, password)
                    if user:
                        login(request, user)
                        return JsonResponse(dict(success=True), safe=False, status=200)
                    return JsonResponse(dict(success=True), safe=False, status=200)
                except:
                    return JsonResponse(dict(success=False, message="Internal Server Error"), safe=False, status=401)
        return JsonResponse(dict(success=False, message="Invalid email or password"), safe=False, status=200)

class Logout(LogoutView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))