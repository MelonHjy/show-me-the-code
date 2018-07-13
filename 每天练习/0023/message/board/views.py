from django.shortcuts import render, redirect
from . import models
import datetime
# Create your views here.


def index(request):
    boardList = models.Board.objects.all()
    return render(request, 'board/index.html', {'boards': boardList})


def submit(request):
    name = request.POST.get('name')
    content = request.POST.get('content')
    date = str(datetime.datetime.now())
    new_board = models.Board(name=name, content=content, date=date)
    new_board.save()
    return redirect('/index')
