from django.shortcuts import render, get_object_or_404
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('league/index.html')
	return render(request, 'league/index.html')