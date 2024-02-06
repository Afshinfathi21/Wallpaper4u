from django.urls import path,include
from .views import  *

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    
]