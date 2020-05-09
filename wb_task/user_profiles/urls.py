from .views import UserProfileCreate, UserProfileUpdate, UserProfileDelete, IndexView
from django.urls import path, include


app_name = "user_profiles"
urlpatterns = [
    path("", IndexView.as_view(), name="user-profile-index"),
    path("create/", UserProfileCreate.as_view(), name="user-profile-create"),
    path("<int:pk>/update/", UserProfileUpdate.as_view(), name="user-profile-update",),
    path("<int:pk>/delete/", UserProfileDelete.as_view(), name="user-profile-delete",),
]
