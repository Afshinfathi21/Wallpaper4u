from django.urls import include, path
from .views import *
from django.contrib.auth import views as auth

urlpatterns = [
    path('signup/',RegisterAPIView.as_view(),name='signup'),
    path('login/',LoginAPIView.as_view(),name='login'),

    path('logout/', auth.LogoutView.as_view(next_page='/'), name ='logout'),
] 