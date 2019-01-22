from rest_framework import serializers

from .models import User, Post, Like


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'posts', 'likes')


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'user', 'content', 'date', 'likes')


class LikeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Like
        fields = ('user', 'post', 'date')
