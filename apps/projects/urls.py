from django.urls import path
from .views import ProjectCreateView, ProjectDeleteView, ProjectsListView, ProjectDetailView, ProjectUpdateView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = 'projects'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('list/', ProjectsListView.as_view(), name='list'),
    path('detail/<slug:slug>/<int:year>/<int:month>/<int:day>/', ProjectDetailView.as_view(), name='detail'),
    path('edit/<slug:slug>/<int:year>/<int:month>/<int:day>/', ProjectUpdateView.as_view(), name='edit'),
    path('confirm_delete/<slug:slug>/<int:year>/<int:month>/<int:day>/', ProjectDeleteView.as_view(), name='delete'),
    path('<slug:slug>/<int:year>/<int:month>/<int:day>/add_task/', TaskCreateView.as_view(), name='create_task'),
    path('edit_task/<slug:slug>/<int:year>/<int:month>/<int:day>/', TaskUpdateView.as_view(), name='edit_task'),
    path('confirm_delete_task/<slug:slug>/<int:year>/<int:month>/<int:day>/', TaskDeleteView.as_view(), name='delete_task'),
]
