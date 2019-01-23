from django.db import models
from django.utils import timezone

class User(models.Model):
    """
    User Model

    """
    email = models.EmailField()
    password = models.CharField(max_length=200)
    last_login = models.DateTimeField('last login', default=timezone.now)

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
