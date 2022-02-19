from django.contrib import admin
from . import models

admin.site.register(models.SubjectsCategory)
admin.site.register(models.Subjects)
admin.site.register(models.Lesson)

