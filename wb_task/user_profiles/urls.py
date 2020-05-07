from .views import UserProfileCreate, UserProfileUpdate, UserProfileDelete, IndexView
from django.urls import path, include


app_name = "user_profiles"
urlpatterns = [
    path("", IndexView.as_view(), name="user-profile-index"),
    path("profile/create/", UserProfileCreate.as_view(), name="user-profile-create"),
    path(
        "profile/update/<int:pk>/",
        UserProfileUpdate.as_view(),
        name="user-profile-update",
    ),
    path(
        "profile/delete/<int:pk>/",
        UserProfileDelete.as_view(),
        name="user-profile-delete",
    ),
]
