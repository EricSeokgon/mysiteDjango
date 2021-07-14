from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
