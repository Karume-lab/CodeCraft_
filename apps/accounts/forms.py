from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from allauth.account.forms import LoginForm, SignupForm
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

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control form-control-lg',
                'id': 'emailAddress',
                'name': 'login',
                'placeholder': 'Email Address'
            }
        )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control form-control-lg',
                'id': 'password',
                'name': 'login',
                'placeholder': 'Password'
            }
        )
        self.fields['login'].label = ''
        self.fields['password'].label = ''

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control form-control-lg',
                'id' : 'username',
                'name': 'username',
                'placeholder': 'Username'
            }
        )
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control form-control-lg',
                'id' : 'emailAddress',
                'name': 'email',
                'placeholder': 'Email Address'
            }
        )

        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control form-control-lg',
                'id': 'password1',
                'name': 'password1',
                'placeholder': 'Password'
            }
        )

        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'type': 'password',
                'class': 'form-control form-control-lg',
                'id': 'password2',
                'name': 'password2',
                'placeholder': 'Password'
            }
        )