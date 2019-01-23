from rest_framework import serializers

from .models import User, Post, Like


class UserSerializer(serializers.ModelSerializer):
    """
    User Serializer

    """
    class Meta:
        model = User
        fields = ('id', 'email', 'posts', 'likes')


class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer

    """
    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'date', 'likes')


class LikeSerializer(serializers.ModelSerializer):
    """
    Like Serializer

    """
    class Meta:
        model = Like
        fields = ('user', 'post', 'date')
