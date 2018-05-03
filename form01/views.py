from django.http import HttpResponse
from django.shortcuts import render

from form01.forms import TestForm, UserModelForm


def test(request):
    test_form = TestForm()


def register(request):
    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        return HttpResponse('验证成功')
    else:
        user_form = UserModelForm()
    return render(request, 'form01.html', {'user_form': user_form})
