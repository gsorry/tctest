from django.utils import timezone
from django.contrib.auth import hashers
from django.conf import settings

from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from pyhunter import PyHunter

from .serializers import UserSerializer, PostSerializer, LikeSerializer

from .models import User, Post, Like


class UserViewSet(ViewSet):
    """
    User View Set

    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    @action(detail=False, methods=['post'], name='User Signup')
    def signup(self, request):
        hunter = PyHunter(settings.HUNTER_API_KEY)
        if (User.objects.filter(email=request.data['email']).exists()):
            return Response({"detail": "Email already taken."}, status=status.HTTP_400_BAD_REQUEST)
        elif hunter.email_verifier(request.data['email']):
            return Response({"detail": "Email not valid."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User(email=request.data['email'],
                        password=hashers.make_password(request.data['password']))
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)


class PostViewSet(ModelViewSet):
    """
    Post View Set

    """
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        user = request.user
        content = request.data['content']
        date = timezone.now()
        post = Post(user=user, content=content, date=date)
        post.save()
        serializer = PostSerializer(post)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'], name='Like Post')
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        date = timezone.now()
        like = Like(user=user, post=post, date=date)
        like.save()
        serializer = PostSerializer(self.get_object())
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='Like Post')
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        date = timezone.now()
        like = Like(user=user, post=post, date=date)
        like.save()
        serializer = LikeSerializer(like)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=True, methods=['get'], name='Unlike Post')
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like = Like.objects.get(user=user, post=post)
        like.delete()
        serializer = LikeSerializer(like)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
