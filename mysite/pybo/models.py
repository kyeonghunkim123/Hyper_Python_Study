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
        self.id = kwarg.get('id')
        self.subject = kwarg.get('subject')
        self.content = kwarg.get('content')
        self.create_date = kwarg.get('create_date')
        # self.id3 = kwarg.get('id3')

class Question2(models.Model):
    id = None
    subject = None
    content = None
    create_date= None
    def __str__(self):
        return self.subject


class Answer1():
    def __init__(self, **kwarg):
        self.question = kwarg.get('question')
        self.content = kwarg.get('content')
        self.create_date = kwarg.get('create_date')

# KKH 추가 230427 끝
