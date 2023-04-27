import pymysql
from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from pymysql.cursors import DictCursor

from .models import Question, Question1
from .utils import select_insert_mysql


# Create your views here.

def index1(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail1(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create1(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)



# KKH 추가 230427 시작


def index(request):
    db = 'For_Study_DB'
    sql = "select id, subject, content, DATE_FORMAT(create_date, '%Y%m%d%H%i%s') as create_date from TBL_Question"
    question_list = select_insert_mysql(request,db, sql, Question1)['question_list']
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)
# KKH 추가 230427 끝