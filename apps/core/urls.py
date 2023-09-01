from django.urls import path

from .views import HomeTemplateView, IndexTemplateView, SearchTemplateView, send_email
from .views import HomeTemplateView, IndexTemplateView, SearchTemplateView, ShareTemplateView, FeedbackTemplateView, RandomizeDetailView


app_name = 'core'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('home/', HomeTemplateView.as_view(), name='home'),
    path('home/search_results/', SearchTemplateView.as_view(), name='search'),
    path('send_email', send_email, name='send_email'),
    path('home/share/', ShareTemplateView.as_view(), name='share'),
    path('home/feedback/', FeedbackTemplateView.as_view(), name='feedback'),
	  path('home/randomize/', RandomizeDetailView.as_view(), name='randomize'),
]
