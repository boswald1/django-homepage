from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Champion

# Create your views here.
def index(request):
	template = loader.get_template('league/index.html')
	return render(request, 'league/index.html')

def champions(request):
	champ_list = Champion.objects.order_by('-name')
	context = { 'champ_list': champ_list }
	return render(request, 'league/champs.html', context)

def detail(request, champ_id):
	try:
		champ = Champion.objects.get(pk=champ_id)
	except Champion.DoesNotExist:
		raise Http404("Champion does not exist")
	return render(request, 'league/detail.html', {'champ': champ})