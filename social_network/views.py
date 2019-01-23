from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, logout

from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, PostSerializer

from .models import User, Post, Like


class UserViewSet(ViewSet):
    """
    User View Set

    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], name='User Signup')
    def signup(self, request):
        if (User.objects.filter(email=request.data['email']).exists()):
            return Response({"detail": "Email already taken."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = User(email=request.data['email'], password=request.data['password'])
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)

    @action(detail=False, methods=['post'], name='User Login')
    def login(self, request):
        user = get_object_or_404(User, email=request.data['email'], password=request.data['password'])
        login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], name='User Logout')
    def logout(self, request):
        logout(request)
        return Response({"detail": "Logout successful."})


class PostViewSet(ModelViewSet):
    """
    Post View Set

    """
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'], name='Like Post')
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        date = timezone.now()
        like = Like(user=user, post=post, date=date)
        like.save()
        serializer = PostSerializer(self.get_object())
        return Response(serializer.data)

    @action(detail=True, methods=['get'], name='Unlike Post')
    def unlike(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like = Like.objects.get(user=user, post=post)
        like.delete()
        serializer = PostSerializer(self.get_object())
        return Response(serializer.data)
