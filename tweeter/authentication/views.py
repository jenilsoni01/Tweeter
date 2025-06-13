from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import SignUpForm, LoginForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.decorators.http import require_POST
from django.contrib import messages

from .models import Profile


# Create your views here.


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a profile for the new user
            Profile.objects.create(user=user)
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "sign_up.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")


def profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=user)
        return render(request, "profile.html", {"profile": profile, "user": user})
    except User.DoesNotExist:
        return redirect("home")


@login_required
def follow_profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        profile_to_follow = get_object_or_404(Profile, user=user)
        current_user_profile = request.user.profile
        if current_user_profile in profile_to_follow.followers.all():
            profile_to_follow.followers.remove(current_user_profile)
        else:
            profile_to_follow.followers.add(current_user_profile)
    return redirect("profile_detail", username=username)


@login_required
def edit_profile(request, username):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect("profile_detail", username=request.user.username)
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, "edit_profile.html", {"form": form})
