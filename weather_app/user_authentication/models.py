from django.db import models
from django.contrib.auth.models import AbstractUser
from checkin.models import Checkin, Clothes

class User(AbstractUser):
    pass
