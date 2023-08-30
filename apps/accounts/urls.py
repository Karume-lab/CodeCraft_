from django.urls import path, include
from .views import MyProfileTamplateView


urlpatterns = [
    path('', include('allauth.urls')),
    path('my-profile/', MyProfileTamplateView.as_view(), name='profile'),
]
