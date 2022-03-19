from django.db import models
from .utils import unique_slug_generator
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.utils import timezone
from django_editorjs_fields import EditorJsTextField

from django.contrib.auth import get_user_model
from exercise.models import Exercise
User = get_user_model()


class Contest(models.Model):
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    organizer = models.CharField(max_length=100)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    date_start = models.DateTimeField(null=False, blank=False)
    date_end = models.DateTimeField(null=False, blank=False)
    password = models.CharField(max_length=20, blank=True, null=True)
    published_on = models.DateTimeField(null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)
    description = EditorJsTextField()

    def __str__(self):
        return self.name


@receiver(post_save, sender=Contest)
def generate_unique_slug_for_posts(sender, instance, created, *args, **kwargs):
    """Update The Slug of 'Slug' When The Exercise Save"""

    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()


@receiver(pre_save, sender=Contest)
def update_published_on(sender, instance, **kwargs):
    """Update The Date Of 'Published On' When The Post Gets Published"""

    if instance.id:
        old_value = Contest.objects.get(pk=instance.id).published_on
        if not old_value:
            instance.published_on = timezone.now()


class ContestDetail(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, null=False, blank=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=False, blank=False)
    score = models.IntegerField()

    def __str__(self):
        return self.contest.name + " | " + self.exercise.name
