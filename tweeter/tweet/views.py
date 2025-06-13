from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Tweet
from .forms import TweetForm


# Create your views here.


def tweet_view(request):
    return render(request, "tweet.html", {"tweets": Tweet.objects.all()})


@login_required
def create_tweet(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("/home/")  # or wherever your homepage is
    else:
        form = TweetForm()
    return render(request, "create.html", {"form": form})


@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect("/home/")
    else:
        form = TweetForm(instance=tweet)
    return render(request, "edit.html", {"form": form, "tweet_id": tweet_id})


@login_required
@require_POST
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    tweet.delete()
    return redirect("/home/")


def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    replies = tweet.replies.all()
    return render(request, "tweet_detail.html", {
        "tweet": tweet,
        "replies": replies,
        "form": TweetForm()
    })


@login_required
@require_POST
def like_tweet(request, tweet_id):
    try:
        tweet = get_object_or_404(Tweet, id=tweet_id)
        profile = request.user.profile
        
        if profile in tweet.likes.all():
            tweet.likes.remove(profile)
        else:
            tweet.likes.add(profile)
        
        return redirect("tweet_detail", tweet_id=tweet.id)

    except Tweet.DoesNotExist:
        return redirect("home")
    except Exception as e:
        print(f"Error liking tweet: {e}")
        return redirect("home")


@login_required
def reply_to_tweet(request, tweet_id):
    parent_tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.parent = parent_tweet
            reply.save()
            return redirect("tweet_detail", tweet_id=tweet_id)
    else:
        form = TweetForm()
    return render(request, "reply.html", {
        "form": form,
        "parent_tweet": parent_tweet
    })


# @login_required
# def 
