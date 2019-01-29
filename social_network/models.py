from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    User Model
    Inherit the Abstract User and overrides some properties

    """
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Post(models.Model):
    """
    Post Model

    """
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField('post date')

    def __str__(self):
        return self.content


class Like(models.Model):
    """
    Like Model

    """
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    date = models.DateTimeField('like date')

    def __str__(self):
        return self.user.email
