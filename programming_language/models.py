from django.db import models

# Create your models here.


class ProgrammingLanguage(models.Model):
    language = models.CharField(max_length=50)
    command = models.CharField(max_length=100)

    def __str__(self):
        return self.language
