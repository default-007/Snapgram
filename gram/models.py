from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    #Create User 
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    #Save User
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.comment


class Post(models.Model):
    image = ImageField(blank=False, manual_crop="800x800")
    name = models.CharField(max_length=144, blank=True, default="Post")
    caption = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(User)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return f"{self.name} - {self.caption}"
