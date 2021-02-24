from . import views
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("user/create", views.UserCreate.as_view())
]