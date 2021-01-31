from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignUpForm
# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid(): 
			user = form.save()
			#user instance created
			auth_login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})