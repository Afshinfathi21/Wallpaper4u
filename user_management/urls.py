from django.urls import path,include
from .views import  *

urlpatterns = [
    path('search/',Search.as_view(),name='search')
    ,path('filter/',Filtering.as_view(),name='filter')
    ,path('upload/',create_post,name='upload')
    ,path('like/<str:post_id>',like,name='like')
    ,path('delete-post:<str:post_id>/',delete_post,name='delete-post'),
    path('profile/<str:user_id>',profile,name='profile')
    
]