from django.contrib import admin
from django.urls import path, re_path, include
from newsapp.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("newspost", NewsPostAPIViewSet, basename="newspost")

urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
]