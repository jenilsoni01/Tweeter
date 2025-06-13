from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import Profile
from django.contrib.auth.models import User
# from

def root(request):
    if request.user.is_authenticated:
        user=get_object_or_404(User, username=request.user.username)
        profile=get_object_or_404(Profile, user=request.user)
        users=User.objects.all()
        return {'profile': profile, 'all_users': users}
    return {}

def home(request):
    redirect('')
    return render(request, 'index.html')
