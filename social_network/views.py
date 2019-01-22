from django.http import HttpResponse, Http404

from rest_framework import viewsets

from .serializers import UserSerializer, PostSerializer, LikeSerializer

from .models import User, Post, Like


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().order_by('-id')
    serializer_class = LikeSerializer
