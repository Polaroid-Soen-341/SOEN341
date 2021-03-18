from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('post/', views.PostListCreate.as_view(), name='posts'),
    path('image/', views.PicturesListCreate.as_view(), name='posts'),
    path('comment/', views.CommentListCreate.as_view(), name='posts'),

    path('post/<uuid:pk>', views.PostInfo.as_view(), name='post'),
    path('image/<uuid:pk>', views.PictureInfo.as_view(), name='image'),
    path('comment/<uuid:pk>', views.CommentInfo.as_view(), name='comment'),
]