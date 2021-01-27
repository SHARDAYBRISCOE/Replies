from django.shortcuts import render, get_object_or_404
from .models import Board
from django.http import Http404


def home(request):
	boards = Board.objects.all()
	return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
	# we included pk in the url.py file so we need it here
	# pk means primary key
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
	board = get_object_or_404(Board, pk=pk)
	return render(request, 'new_topic.html', {'board': board})