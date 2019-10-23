from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=40)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=40)
    
    def __str__(self):
        return self.answer
    

class User(models.Model):
    name = models.CharField(max_length= 20)
    email = models.CharField(max_length= 20)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name

class QuestionAndAnswer(models.Model):
    feedback = models.BooleanField(default=True)
    answer = models.ForeignKey(Answer, default=None, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default= None, on_delete=models.CASCADE)
    data = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.answer.answer
