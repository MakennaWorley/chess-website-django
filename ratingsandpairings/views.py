from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import generic
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(generic.FormView):
    form_class = LoginForm
    template_name = "landingpage.html"
    success_url = "/home/"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            print("Invalid username or password")
            form.add_error(None, "Invalid username or password")
            return self.form_invalid(form)


class HomeView(LoginRequiredMixin, generic.TemplateView):
    login_url = "/"
    template_name = "homepage.html"