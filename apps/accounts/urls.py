from django.urls import path, include
from .views import MyProfileTamplateView, ProfileUpdateView


urlpatterns = [
    path('', include('allauth.urls')),
    path('my-profile/', MyProfileTamplateView.as_view(), name='profile'),
	path('edit-profile/<str:email>', ProfileUpdateView.as_view(), name='edit-profile'),
]
