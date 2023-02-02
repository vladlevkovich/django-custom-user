from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')

    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password do not math')
        return cd['password2']


