from django.db import models
from authentication.models import UserProfile

class Survey(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

class Response(models.Model):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text
