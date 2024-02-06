from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from user_management.models import *

class Home(ListView):
    model=Post
    template_name="home.html"
    def get_queryset(self):
        object_list=Post.objects.all()
        return object_list
    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super(Home, self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()

        if isinstance(user, CustomUser):
            liked_posts_ids = Like.objects.filter(user=user).values_list('post__id', flat=True)
            context['post_liked'] = Post.objects.filter(id__in=liked_posts_ids)
        else:
            context['post_liked'] = Post.objects.none()

        return context
    
from django.db.models import Count,Sum
@login_required(login_url='login')    
def dashboard(request):
    user=request.user
    category=Category.objects.all()
    posts=Post.objects.filter(user=user).annotate(total_likes=Count('likes'))
    total_likes = posts.aggregate(sum_likes=Sum('total_likes'))
    likes=Like.objects.filter(user=user)
    context={
        'user':user,
        'categorys':category,
        'posts':posts,
        'likes':likes,
        'total_like':total_likes
    }
    return render(request,'dashboard-base.html',context)