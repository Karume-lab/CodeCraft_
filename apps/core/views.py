from django.shortcuts import render
from allauth.account.views import LoginView
from django.views.generic import TemplateView
# Create your views here.
class IndexView(TemplateView):
    template_name = 'core/index.html'

class HomeView(TemplateView):
    template_name = 'core/home.html'
