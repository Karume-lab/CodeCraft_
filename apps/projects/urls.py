from django.urls import path
from .views import ProjectCreateView, ProjectDeleteView, ProjectsListView, ProjectDetailView, ProjectUpdateView

app_name = 'projects'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('list/', ProjectsListView.as_view(), name='list'),
    path('detail/<slug:slug>/<int:year>/<int:month>/<int:day>/', ProjectDetailView.as_view(), name='detail'),
    path('edit/<slug:slug>/<int:year>/<int:month>/<int:day>/', ProjectUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/<int:year>/<int:month>/<int:day>/', ProjectDeleteView.as_view(), name='delete'),
]
