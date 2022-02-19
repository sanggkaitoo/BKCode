from django.db import models
from django_editorjs_fields import EditorJsTextField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from .utils import unique_slug_generator
from .utils import unique_slug_generator2


class SubjectsCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subjects(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SubjectsCategory, on_delete=models.CASCADE, null=False, blank=False)
    slug = models.SlugField(blank=True, null=True, unique=True)
    logo = models.ImageField(upload_to='uploads/subjects_logo', null=False, blank=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Subjects)
def generate_unique_slug_for_posts(sender, instance, created, *args, **kwargs):
    """Update The Slug of 'Slug' When The Lesson Save"""

    if created:
        instance.slug = unique_slug_generator2(instance)
        instance.save()


class Lesson(models.Model):
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=False, blank=False)
    section = models.CharField(max_length=200, unique=True)
    content = EditorJsTextField()
    slug = models.SlugField(blank=True, null=True, unique=True)
    section_order = models.IntegerField(blank=False, null=False, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject.name + ' - Lesson ' + str(self.section_order) + ' - ' + self.section


@receiver(post_save, sender=Lesson)
def generate_unique_slug_for_posts(sender, instance, created, *args, **kwargs):
    """Update The Slug of 'Slug' When The Lesson Save"""

    if created:
        instance.slug = str(instance.subject.slug) + '-' + str(instance.section_order) + '-' + unique_slug_generator(instance)
        instance.save()


@receiver(pre_save, sender=Lesson)
def update_published_on(sender, instance, **kwargs):
    """Update The Date Of 'Published On' When The Lesson Gets Published"""

    if instance.id:
        old_value = Lesson.objects.get(pk=instance.id).published_on
        if not old_value:
            instance.published_on = timezone.now()
