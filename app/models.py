from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Question(models.Model):
    S_No=models.IntegerField(primary_key=True)
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.TextField()

    def __str__(self) -> str:
        return self.question
    
class Answer(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.answer
    
    
