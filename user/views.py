import itertools
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from .forms import LoginForm

UserModel = get_user_model()

# Create your views here.
class LoginOrSignup(LoginView):
    form_class = LoginForm
    http_method_names = ['post']

    def _login(self, request, user):
        login(request, user)
        messages.add_message(request, messages.INFO, '{0} logged in.'.format(user.email))
        return JsonResponse(dict(success=True, user=dict(email=user.email)), safe=False, status=status.HTTP_200_OK)
    
    def _response_error(self, messages, status_code):
        return JsonResponse(dict(success=False, messages=messages), safe=False, status=status_code)

    def _response_invalid_email_or_password(self, request):
        return self._response_error(["Invalid email or password"], status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                return self._login(request, user)
            return self._response_invalid_email_or_password(request)  
        else:
            error_messages = list(itertools.chain(*list(form.errors.values())))
            return self._response_error(error_messages, status.HTTP_400_BAD_REQUEST)

class Logout(LogoutView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, 'Logged out successfully.')
        logout(request)
        return HttpResponseRedirect(reverse('index'))