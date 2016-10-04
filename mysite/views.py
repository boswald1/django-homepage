from django.shortcuts import render, get_object_or_404
from django.template import loader

def index(request):
	page_title = "Homepage"
	context = { 'page_title': page_title }
	return render(request, 'mysite/index.html', context)


def resume(request):
	page_title = "My Resume"
	context = { 'page_title': page_title }
	return render(request, 'mysite/resume.html', context)


