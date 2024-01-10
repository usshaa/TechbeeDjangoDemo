from django.shortcuts import render,redirect
from .forms import UserProfileForm,CustomUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# Create your views here.
def user_signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request,user)
            return redirect('profile')
    else:
        form = CustomUserForm()
    return render(request,'signup.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})
    

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    form = UserProfileForm(instance=request.user.userprofile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=request.user.userprofile)
        if form.is_valid():
            form.save()
    return render(request,'profile.html',{'user':request.user,'form':form})
        