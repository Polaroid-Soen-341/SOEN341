from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('post/<str:uuid_i>', views.index, name='index'),
    path('image/<str:uuid_i>', views.index, name='index'),
    path('comment/<str:uuid>', views.index, name='index'),
]