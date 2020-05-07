from cities_light.models import City
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


phone_number_validator = RegexValidator(
    regex=r"^\(?(?:\+44)?\)?[#()\s\d-]{,24}$",
    message="Please enter a valid UK phone number.",
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    address_line_1 = models.CharField(
        max_length=256, help_text="Street name and number."
    )
    address_line_2 = models.CharField(blank=True, null=True, max_length=256)
    address_postcode = models.CharField(max_length=8, verbose_name="Postcode")
    address_city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name="City"
    )
    phone_number = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        validators=[phone_number_validator],
        help_text="Valid UK phone number.",
    )
    mobile_number = models.CharField(
        max_length=32,
        validators=[phone_number_validator],
        help_text="Valid UK mobile number.",
    )
