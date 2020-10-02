from django.contrib.auth import views
from django.urls import path
from .views import *


urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('ru/', RuView.as_view(), name='ru'),
    path('euro/', EuroView.as_view(), name='euro'),
    path('free/', FreeView.as_view(), name='free'),
    path('', HomeView.as_view()),
    path('home/', HomeView.as_view(), name='home'),
    path('user/', UserView.as_view(), name='user'),
    path('all-users/', AllUsersView.as_view(), name='all-users'),
    path('notifications/', NotificationsView.as_view(), name='notifications'),
    path('signup/', signup, name='signup'),
    path('', LogoutView.as_view(), name='signout'),
    ]