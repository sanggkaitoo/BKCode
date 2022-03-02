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
    # status_list = (
    #     ("AC", "Accepted"),
    #     ("WA", "Wrong Answer"),
    #     ("CE", "Compile Error"),
    #     ("TLE", "Time Limit Exceeded"),
    #     ("MLE", "Memory Limit Exceeded"),
    #     ("RE", "Runtime Error"),
    #     ("SE", "System Error")
    # )
    status_list = (
        ("OK", "OK"),
        ("ACCEPTED", "ACCEPTED"),
        ("WRONG ANSWER", "WRONG ANSWER"),
        ("COMPILATION ERROR", "COMPILATION ERROR"),
        ("RUNTIME ERROR", "RUNTIME ERROR"),
        ("INVALID FILE", "INVALID FILE"),
        ("FILE NOT FOUND", "FILE NOT FOUND"),
        ("TIME LIMIT EXCEEDED", "TIME LIMIT EXCEEDED")
    )
    status = models.CharField(choices=status_list, max_length=40)
    time = models.IntegerField()
    memory = models.IntegerField()
    date_submit = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    notes = models.TextField()
