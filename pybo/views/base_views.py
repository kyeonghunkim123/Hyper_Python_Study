from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question

def index(request):
    # -create_date로 해야 먼저작성한 글이 밀려 내려가게됨
    page = request.GET.get('page', '1') # 페이지
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}  # question_list는 페이징 객체(page_obj)
    # context = {'question_list': question_list} # 위에 context 사용으로 전에 써둔거 off
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # pk = primary key 에 해당하는 값
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)