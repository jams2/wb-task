from .models import UserProfile
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings


class IndexView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        if not hasattr(self.request.user, "userprofile"):
            return reverse("user_profiles:user-profile-create")
        return reverse("user_profiles:user-profile-update", args=[self.request.user.id])


class ProfileOwnerMixin:
    login_url = settings.LOGIN_URL

    def dispatch(self, *args, **kwargs):
        if not hasattr(self.request.user, "userprofile"):
            return super().dispatch(*args, **kwargs)
        elif "pk" in kwargs and kwargs["pk"] != self.request.user.userprofile.pk:
            return redirect("user_profiles:user-profile-index")
        return super().dispatch(*args, **kwargs)


class UserProfileCreate(
    ProfileOwnerMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    login_url = settings.LOGIN_URL
    success_message = "Your profile was created."
    model = UserProfile
    fields = [
        "first_name",
        "last_name",
        "mobile_number",
        "phone_number",
        "address_line_1",
        "address_line_2",
        "address_postcode",
        "address_city",
    ]

    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.pk)
        form.instance.user = user
        return super().form_valid(form)


class UserProfileUpdate(
    ProfileOwnerMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    login_url = settings.LOGIN_URL
    success_message = "Your profile was updated."
    model = UserProfile
    fields = [
        "first_name",
        "last_name",
        "mobile_number",
        "phone_number",
        "address_line_1",
        "address_line_2",
        "address_postcode",
        "address_city",
    ]


class UserProfileDelete(ProfileOwnerMixin, LoginRequiredMixin, DeleteView):
    login_url = settings.LOGIN_URL
    model = UserProfile
    success_url = "/"

    def delete(self, *args, **kwargs):
        """ As the UserProfile is a proxy to the User, delete them both
        here.
        """
        self.request.user.delete()
        messages.success(self.request, "Your account was deleted.")
        logout(self.request)
        return redirect("/")
