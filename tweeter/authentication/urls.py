from django.urls import path
from . import views

urlpatterns = [
    path("auth/signup/", views.signup_view, name="signup"),
    path("auth/login/", views.login_view, name="login"),
    path("auth/logout/", views.logout_view, name="logout"),
    path("profile/<str:username>/", views.profile_view, name="profile_detail"),
    # path("profile/<str:username>/follow/", views.follow_profile, name="follow_profile"),
    path("profile/<str:username>/edit/", views.edit_profile, name="edit_profile"),
]