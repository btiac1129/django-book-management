from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True,
                                    validators=[RegexValidator(r'^010-?\d{4}-?\d{4}$')])

    