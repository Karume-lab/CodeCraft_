from django.urls import path, include
from .views import HomeView, IndexView

app_name = 'core'
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('home/', HomeView.as_view(), name='home'),
]
