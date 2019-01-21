from django.db import models

class Post(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateTimeField('post date')

    def __str__(self):
        return self.content


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField('post date')
