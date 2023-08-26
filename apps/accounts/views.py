from django.shortcuts import render
from allauth.account.views import LoginView

# Create your views here.
class CustomLoginView(LoginView):
    def form_valid(self, form):
        if self.request.method == 'POST':
            pass
        else:
            pass
