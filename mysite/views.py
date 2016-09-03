from django.shortcuts import render, get_object_or_404
from django.template import loader

def index(request):
	template = loader.get_template('mysite/index.html')
	return render(request, 'mysite/index.html')