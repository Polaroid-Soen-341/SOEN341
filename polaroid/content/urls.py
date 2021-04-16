from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('post/', views.PostListCreate.as_view(), name='post'),
    path('comment/', views.CommentListCreate.as_view(), name='comment'),

    path('post/user/<str:pk>', views.PostUserInfo.as_view(), name='post_user'),
    path('comment/user/<str:pk>', views.CommentUserInfo.as_view(), name='comment_user'),

    path('post/<uuid:pk>', views.PostInfo.as_view(), name='post_id'),
    path('comment/<uuid:pk>', views.CommentInfo.as_view(), name='comment_id'),
]