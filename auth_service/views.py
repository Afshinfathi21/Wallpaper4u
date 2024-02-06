from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from user_management.models import Category,Post,Like
from .models import *
from .forms import *
from email_service.views import activateEmail


class RegisterAPIView(APIView):
    def post(self, request):
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return render(request, 'waiting_for_confirmation.html')
        else:
            return render(request, 'signup.html', {'form': form})
    def get(self,request):
        form = UserCreationForm()
        return render(
            request=request,
            template_name="signup.html",
            context={"form": form}
        )

class LoginAPIView(APIView):
    def post(self, request):
        next_url = request.GET.get('next', '/')
        form = UserloginForm(request=request, data=request.data)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            if user is not None:
                login(request, user)
                messages.success(
                     request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect(next_url)
            else:
                messages.error(request, "Invalid login credentials")
        else:
            return render(request, 'login.html', {'form': form})
    def get(self,request):
        form=UserloginForm()
        return render(request,'login.html',{'form':form})

