from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from wb_task.views import IndexView
from wb_task.user_profiles.models import UserProfile
from tests.factory import UserFactory, UserProfileFactory


class TestClientTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = UserFactory()


class TestIndexView(TestClientTestCase):
    def test_unauthenticated_user_not_redirected(self):
        """ An unauthenticated user should get the default login
        index page.
        """
        self.client.logout()
        response = self.client.get("/", follow=True)
        self.assertEqual(200, response.status_code)

    def test_authenticated_user_redirected(self):
        """ A logged in user should be redirected to the user profile
        redirect view.
        """
        self.client.force_login(self.user)
        response = self.client.get("/", follow=True)
        self.assertEqual(("/profile/", 302), response.redirect_chain[0])


class TestUserProfileViews(TestClientTestCase):
    def test_user_profile_creation_redirect(self):
        """ A user without a UserProfile should be redirected to the
        creation form.
        """
        UserProfile.objects.all().delete()
        self.client.force_login(self.user)
        response = self.client.get("/profile/", follow=True)
        self.assertEqual(("/profile/create/", 302), response.redirect_chain[0])

    def test_user_profile_update_redirect(self):
        """ A user with an existing UserProfile should be redirect to
        the update form.
        """
        profile = UserProfileFactory(user=self.user)
        self.client.force_login(self.user)
        response = self.client.get("/profile/", follow=True)
        self.assertEqual(
            (f"/profile/{profile.pk}/update/", 302), response.redirect_chain[0]
        )

    def test_user_without_profile_redirected_from_delete(self):
        """ A user without a UserProfile should not be able to access
        the UserProfileDelete view.
        """
        UserProfile.objects.all().delete()
        self.client.force_login(self.user)
        response = self.client.get("/profile/1/delete/")

    def test_user_accesses_only_own_profile(self):
        user_profile = UserProfileFactory(user=self.user)
        user_2 = UserFactory(username="Jane Citizen")
        user_profile_2 = UserProfileFactory(user=user_2)
        self.client.force_login(user_2)
        response = self.client.get(f"/profile/{user_profile.pk}/update/", follow=True)
        self.assertEqual((f"/profile/", 302), response.redirect_chain[0])
