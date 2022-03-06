from django.urls import path

from management import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('all_clubs', views.all_clubs, name='all_clubs'),
    path('my_clubs', views.my_clubs, name='my_clubs'),
    path('favorites', views.favorites, name='favorites'),
    path('analytics', views.analytics, name='analytics'),
    path('documents', views.documents, name='documents'),
    path('settings', views.settings, name='settings'),
    path('club-info/<int:club_id>', views.club_info, name='club_info'),



]