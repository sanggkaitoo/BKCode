from django.db import models
from django_editorjs_fields import EditorJsTextField


class AboutUs(models.Model):
    description = EditorJsTextField()
