from django.urls import path, include
from .views import HomeView

app_name = 'core'
urlpatterns = [
	path('home/', HomeView.as_view(), name='home'),
]
