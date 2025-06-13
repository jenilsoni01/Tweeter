from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import Profile
from django.contrib.auth.models import User
# from

def root(request):
    users=User.objects.all()
    if request.user.is_authenticated:
        user=get_object_or_404(User, username=request.user.username)
        profile=get_object_or_404(Profile, user=request.user)
        return {'profile': profile, 'all_users': users}
    return {'all_users': users}

def home(request):
    redirect('')
    return render(request, 'index.html')
