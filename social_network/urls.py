from django.urls import path

from . import views


urlpatterns = [
    path('', views.users, name='users'),
    path('login/', views.users_login, name='users_login'),
    path('signup/', views.users_signup, name='users_signup'),
    path('posts/', views.posts, name='posts'),
    path('posts/create/', views.posts_create, name='posts_create'),
    path('posts/like/<int:post_id>/', views.posts_like, name='posts_like'),
    path('posts/unlike/<int:post_id>/', views.posts_unlike, name='posts_unlike'),
]
