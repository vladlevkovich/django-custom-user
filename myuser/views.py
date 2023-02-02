from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.views.generic import FormView, CreateView
from . import forms


# class SignupView(CreateView):
#     form_class = forms.SignupForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            return redirect('/')

    else:
        form = forms.RegisterForm()

    return render(request, 'registration/signup.html', {'form': form})



