from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from users.forms import UserCreationForm
# Create your views here.
from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = 'users/registration/login.html'


class Register(View):
    template_name = 'users/registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('user')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
