from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Champion

# Create your views here.
def index(request):
	page_title = "League of Legends Information Station"
	context = {
		'page_title': page_title,
	}
	return render(request, 'league/index.html', context)

def champions(request):
	champ_list = Champion.objects.order_by('name')
	page_title = "Champion List"
	context = {
		'champ_list': champ_list,
		'page_title': page_title,
	}
	return render(request, 'league/champs.html', context)

def detail(request, champ_id):
	try:
		champ = Champion.objects.get(pk=champ_id)
	except Champion.DoesNotExist:
		raise Http404("Champion does not exist")

	page_title = champ.name
	context = {
		'champ': champ,
		'page_title': page_title,
	}
	return render(request, 'league/detail.html', context)


# REST API views
from league.serializers import ChampionSerializer
from rest_framework import generics, status, viewsets

class ChampionList(generics.ListCreateAPIView):
	"""
	List all champions, or create a new champion
	"""
	queryset = Champion.objects.all()
	serializer_class = ChampionSerializer

class ChampionDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a champion instance.
    """
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

