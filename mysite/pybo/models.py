from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()






# Create your models here.

# KKH 추가 230427 시작
class Question1():
    def __init__(self, **kwarg):
        self.id = kwarg['id']
        self.subject = kwarg['subject']
        self.content = kwarg['content']
        self.create_date = kwarg['create_date']


class Answer1():
    def __init__(self, **kwarg):
        self.question = kwarg['question']
        self.content = kwarg['content']
        self.create_date = kwarg['create_date']

# KKH 추가 230427 끝
