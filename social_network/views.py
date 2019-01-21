from django.http import HttpResponse


def users(request):
    users = "Users"
    return HttpResponse(users)


def users_signup(request):
    users = "Users Signup"
    return HttpResponse(users)


def users_login(request):
    users = "Users Login"
    return HttpResponse(users)


def posts(request):
    posts = "Posts"
    return HttpResponse(posts)


def posts_create(request):
    posts = "Posts Create"
    return HttpResponse(posts)


def posts_like(request, post_id):
    posts = "Posts Like %s" % post_id
    return HttpResponse(posts)


def posts_unlike(request, post_id):
    posts = "Posts Unlike %s" % post_id
    return HttpResponse(posts)
