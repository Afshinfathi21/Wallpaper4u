
# Create your views here.
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import *
from .models import Post
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PostForm
from rest_framework.decorators import api_view


def profile(request,user_id):
    req_user=request.user
    user=CustomUser.objects.get(pk=user_id)
    posts=Post.objects.filter(user=user)
    if isinstance(req_user, CustomUser):
            liked_posts_ids = Like.objects.filter(user=req_user).values_list('post__id', flat=True)
            post_liked = Post.objects.filter(id__in=liked_posts_ids)
    else:
            post_liked = Post.objects.none()
    context={
        'user':user,
        'posts':posts,
        'post_liked':post_liked
    }
    return render(request,'profile.html',context)



class Search(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(placeholder__icontains=query) |
            Q(user__username__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context
    
class Filtering(ListView):
    model=Post
    template_name='home.html'
    def get_queryset(self):
        query=self.request.GET.get('c')
        object_list=Post.objects.filter(
            Q(category__name__icontains=query)
        )
        return object_list
    def get_context_data(self,**kwargs):
        context = super(Filtering,self).get_context_data(**kwargs)
        context['categorys'] = Category.objects.all()
        return context

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

@login_required(login_url='login')
def like(request, post_id):
    next_url = request.GET.get('next', '/')
    post = get_object_or_404(Post, pk=post_id)
    like_exists = Like.objects.filter(user=request.user, post=post).exists()

    if like_exists:
        Like.objects.filter(user=request.user, post=post).delete()
    else:
        Like.objects.create(user=request.user, post=post)

    return redirect(next_url)

@login_required(login_url='login')
@api_view(['GET','POST'])
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('home')
    if request.method=='GET':
        form = PostForm()
        return render(request, 'upload.html', {'form': form})
    


@login_required(login_url='login')
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('dashboard')
def profile(request,user_id):
    req_user=request.user
    user=CustomUser.objects.get(pk=user_id)
    posts=Post.objects.filter(user=user)
    if isinstance(req_user, CustomUser):
            liked_posts_ids = Like.objects.filter(user=req_user).values_list('post__id', flat=True)
            post_liked = Post.objects.filter(id__in=liked_posts_ids)
    else:
            post_liked = Post.objects.none()
    context={
        'user':user,
        'posts':posts,
        'post_liked':post_liked
    }
    return render(request,'profile.html',context)