from django.db import models
from django.contrib.auth import get_user_model
from exercise.models import Exercise
from .utils import unique_slug_generator
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

User = get_user_model()


class Class(models.Model):
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    term = models.IntegerField(null=False, blank=False)
    teacher = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + str(self.term) + " - " + self.teacher.username


@receiver(post_save, sender=Class)
def generate_unique_slug_for_posts(sender, instance, created, *args, **kwargs):
    """Update The Slug of 'Slug' When The Exercise Save"""

    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()


class Student_Class(models.Model):
    class_obj = models.ForeignKey(Class, blank=False, null=False, on_delete=models.CASCADE)
    student = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)


class Problem_Class(models.Model):
    class_obj = models.ForeignKey(Class, blank=False, null=False, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, blank=False, null=False, on_delete=models.CASCADE)
