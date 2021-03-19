from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("user/create", views.UserCreate.as_view()),
    path("user/authenticate", views.UserAuth.as_view()),
    path("user/getAll", views.GetUsers.as_view()),
    path("user/follow/<str:username>", views.follow_user),
    path("user/following/", views.GetFollowingUser.as_view()),
    path("user/following/<str:pk>", views.GetFollowingUsers.as_view()),
]