from django.db import models
from django.contrib.auth.models import AbstractUser


class registrationModel(AbstractUser):
    mobile_number = models.CharField(max_length=10, blank=False)
