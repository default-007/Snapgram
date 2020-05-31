from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    profile_pic = ImageField(blank=True, manual_crop="800x800")