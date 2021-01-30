from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post
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
	user = User.objects.first()
	#get the current logged in User
	if request.method == 'POST':
		form = NewTopicForm(request.POST)
		#We are checking if the request is POST or GET
		if form.is_valid():
			#We are asking Django to check the data
			topic = form.save(commit=False)
			topic.board = board
			topic.starter = user
			topic.save()
			post = Post.objects.create(
				message=form.cleaned_data.get('message'),
				topic=topic,
				created_by=user
			)
			return redirect('board_topics', pk=board.pk) # redirect to the created topic page
	else:
		form = NewTopicForm()
	return render(request, 'new_topic.html', {'board': board, 'form': form})