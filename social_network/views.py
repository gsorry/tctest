from django.http import HttpResponse, Http404

from .models import User, Post, Like


def users(request):
    users = User.objects.order_by('id')
    output = ', '.join([u.email for u in users])
    return HttpResponse(output)


def users_signup(request):
    output = "Users Signup"
    return HttpResponse(output)


def users_login(request):
    output = "Users Login"
    return HttpResponse(output)


def posts(request):
    posts = Post.objects.order_by('date')
    output = '; '.join([p.content for p in posts])
    return HttpResponse(output)


def posts_view(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exiast!")
    output = "Posts %s" % post.id
    return HttpResponse(output)


def posts_create(request):
    output = "Posts Create"
    return HttpResponse(output)


def posts_like(request, post_id):
    output = "Posts Like %s" % post_id
    return HttpResponse(output)


def posts_unlike(request, post_id):
    output = "Posts Unlike %s" % post_id
    return HttpResponse(output)
