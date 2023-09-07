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
        self.fields['login'].widget = forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control form-control-lg',
                'id': 'username_emailAddress',
                'name': 'login',
                'placeholder': 'Username or Email Address'
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
                'id': 'username',
                'name': 'username',
                'placeholder': 'Username'
            }
        )
        self.fields['email'].widget = forms.EmailInput(
            attrs={
                'type': 'email',
                'class': 'form-control form-control-lg',
                'id': 'emailAddress',
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

        self.fields['first_name'].widget = forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control form-control-lg',
                'id': 'first_name',
                'name': 'first_name',
                'placeholder': 'First Name'
            }
        )

        self.fields['last_name'].widget = forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'form-control form-control-lg',
                'id': 'last_name',
                'name': 'last_name',
                'placeholder': 'Last Name'
            }
        )
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''


    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
