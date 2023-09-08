from django.urls import path

from .views import (
                        send_email,
                        HomeListView,
                        IndexTemplateView,
                        SearchTemplateView,
                        RandomizeDetailView,
                        ImportantProjectsListView,
						MissedDealineProjectsListView
					)



app_name = 'core'
urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('home/', HomeListView.as_view(), name='home'),
    path('home/search_results/', SearchTemplateView.as_view(), name='search'),
    path('send_email', send_email, name='send_email'),
    path('home/randomize/', RandomizeDetailView.as_view(), name='randomize'),
	path('home/important_projects/', ImportantProjectsListView.as_view(), name='important'),
	path('home/missed_deadline/', MissedDealineProjectsListView.as_view(), name='deadline'),
]
