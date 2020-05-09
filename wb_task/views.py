from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


class IndexView(TemplateView):
    template_name = "index.html"

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse("user_profiles:user-profile-index"))
        return super().dispatch(*args, **kwargs)
