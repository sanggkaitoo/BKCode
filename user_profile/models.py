import os

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


def change_name_file_avatar(instance, filename):
    upload_to = 'user.{}/'.format(instance.user.username)
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(instance.user.username, ext)

    return os.path.join(upload_to, filename)


class UserProfile(models.Model):
    """Model For Extending Default Django User Model"""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    github = models.URLField(blank=True, default="")
    bio = models.TextField(blank=True, max_length=200, default="")
    facebook_url = models.URLField(blank=True, default="")
    avatar = models.ImageField(upload_to=change_name_file_avatar)
    school = models.CharField(blank=True, max_length=100)
    major = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def username(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    """Automatically Create A User Profile When A New User IS Registered"""

    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()
