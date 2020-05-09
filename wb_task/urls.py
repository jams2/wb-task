from django.contrib import admin
from django.urls import path, include
from wb_task.views import IndexView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("profile/", include("wb_task.user_profiles.urls", namespace="user_profiles")),
    path("", IndexView.as_view()),
]
