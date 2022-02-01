from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models.fields import DateTimeField
from programming_language.models import ProgrammingLanguage

from exercise.models import Exercise


User = get_user_model()


class CodeSubmission(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    code = models.TextField()
    status = models.BooleanField()
    time = models.IntegerField()
    memory = models.IntegerField()
    date_submit = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
