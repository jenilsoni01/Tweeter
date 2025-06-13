from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_view, name="tweet"),
    path("create/", views.create_tweet, name="create_tweet"),
    path("<int:tweet_id>/edit/", views.edit_tweet, name="edit_tweet"),
    path("<int:tweet_id>/delete/", views.delete_tweet, name="delete_tweet"),
    path("<int:tweet_id>/", views.tweet_detail, name="tweet_detail"),
    path("<int:tweet_id>/like/", views.like_tweet, name="like_tweet"),
    path("<int:tweet_id>/reply/", views.reply_to_tweet, name="reply_to_tweet"),
]