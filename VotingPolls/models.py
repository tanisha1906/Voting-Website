# models.py
from django.db import models
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user} voted on {self.question}"
