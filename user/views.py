from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse

UserModel = get_user_model()

# Create your views here.
class LoginOrSignup(LoginView):
    http_method_names = ['post']

    def _login(self, request, user):
        login(request, user)
        messages.add_message(request, messages.INFO, '{0} logged in.'.format(user.email))
        return JsonResponse(dict(success=True), safe=False, status=200)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user and user.is_active:
                return self._login(request, user)
            else:
                # Tries to create a new user and add them to the database
                try:
                    user = UserModel.objects.create_user(email, password)
                    if user:
                        return self._login(request, user)
                except:
                    return JsonResponse(dict(success=False, message="Internal Server Error"), safe=False, status=401)
        return JsonResponse(dict(success=False, message="Invalid email or password"), safe=False, status=200)

class Logout(LogoutView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, 'Logged out successfully.')
        logout(request)
        return HttpResponseRedirect(reverse('index'))