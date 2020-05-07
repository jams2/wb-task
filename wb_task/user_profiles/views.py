from .models import UserProfile
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings


class IndexView(LoginRequiredMixin, RedirectView):
    login_url = settings.LOGIN_URL

    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(self.login_url)
        return super().dispatch(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        if not hasattr(self.request.user, "userprofile"):
            return reverse("user_profiles:user-profile-create")
        return reverse("user_profiles:user-profile-update", args=[self.request.user.id])


class UserProfileCreate(LoginRequiredMixin, CreateView):
    login_url = settings.LOGIN_URL
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


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    login_url = settings.LOGIN_URL
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


class UserProfileDelete(LoginRequiredMixin, DeleteView):
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
