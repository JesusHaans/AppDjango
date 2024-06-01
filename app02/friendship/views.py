from django.shortcuts import render
from registration.models import Profile
from django.contrib.auth.models import User
from .models import FriendRequest, Friendship


# Create your views here.

def friendrequest_list(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    friend_requests = FriendRequest.objects.filter(to_user=profile)
    return render(request, 'friendship/friendrequest_list.html', {'friendrequest_list': friend_requests})


def friend_list(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    friends = Friendship.objects.filter(user1=profile)
    return render(request, 'friendship/friendship_list.html', {'friend_list': friends})
    