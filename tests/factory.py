from cities_light.models import City, Country
from django.conf import settings
from factory.django import DjangoModelFactory
from factory import SubFactory
from wb_task.user_profiles.models import UserProfile


class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    name_ascii = "stub"


class CityFactory(DjangoModelFactory):
    class Meta:
        model = City

    country = SubFactory(CountryFactory)
    name_ascii = "stub"


class UserFactory(DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ("username",)

    username = "John Doe"


class UserProfileFactory(DjangoModelFactory):
    class Meta:
        model = UserProfile

    address_city = SubFactory(CityFactory)
