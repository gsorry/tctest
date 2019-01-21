from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField('post date')

    def __str__(self):
        return self.content


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField('like date')

    def __str__(self):
        return self.user.email
