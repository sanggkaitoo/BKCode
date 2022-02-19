from django.db import models
from django.contrib.auth import get_user_model
from django_editorjs_fields import EditorJsTextField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from .utils import unique_slug_generator
from programming_language.models import ProgrammingLanguage

User = get_user_model()


class CategoryExercise(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    slug = models.SlugField(blank=True, null=True, unique=True)
    title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(CategoryExercise, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=100)
    level_choice = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    )
    level = models.CharField(choices=level_choice, max_length=6)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', related_query_name='post')
    question = EditorJsTextField()
    input = EditorJsTextField()
    output = EditorJsTextField()
    test_case = models.TextField(null=True, blank=True)
    output_test_case = models.TextField()
    language = models.ManyToManyField(ProgrammingLanguage)
    memory_limits = models.IntegerField()
    time_limits = models.IntegerField()
    is_published = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    published_on = models.DateTimeField(null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Exercise)
def generate_unique_slug_for_posts(sender, instance, created, *args, **kwargs):
    """Update The Slug of 'Slug' When The Exercise Save"""

    if created:
        instance.slug = unique_slug_generator(instance)
        instance.save()


@receiver(pre_save, sender=Exercise)
def update_published_on(sender, instance, **kwargs):
    """Update The Date Of 'Published On' When The Post Gets Published"""

    if instance.id:
        old_value = Exercise.objects.get(pk=instance.id).published_on
        if not old_value:
            instance.published_on = timezone.now()
