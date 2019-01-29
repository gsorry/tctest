from rest_framework import serializers

from .models import User, Post, Like


class UserSerializer(serializers.ModelSerializer):
    """
    User Model Serializer

    """
    class Meta:
        model = User
        fields = ('id', 'email', 'posts', 'likes')


class PostSerializer(serializers.ModelSerializer):
    """
    Post Model Serializer

    """
    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'date', 'likes')


class LikeSerializer(serializers.ModelSerializer):
    """
    Like Model Serializer

    """
    class Meta:
        model = Like
        fields = ('user', 'post', 'date')
