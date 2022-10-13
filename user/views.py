from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status

UserModel = get_user_model()

# Create your views here.
class LoginOrSignup(LoginView):
    http_method_names = ['post']

    def _login(self, request, user):
        login(request, user)
        messages.add_message(request, messages.INFO, '{0} logged in.'.format(user.email))
        return JsonResponse(dict(success=True, user=dict(email=user.email)), safe=False, status=status.HTTP_200_OK)
    
    def _response_invalid_email_or_password(self, request):
        msg = "Invalid email or password"
        return JsonResponse(dict(success=False, message=msg), safe=False, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                return self._login(request, user)
            return self._response_invalid_email_or_password(request)

class Logout(LogoutView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, 'Logged out successfully.')
        logout(request)
        return HttpResponseRedirect(reverse('index'))