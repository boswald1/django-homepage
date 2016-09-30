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
	base_url = "//ddragon.leagueoflegends.com/cdn/6.18.1/img/champion/"
	context = {
		'champ_list': champ_list,
		'page_title': page_title,
		'base_url': base_url,
	}
	return render(request, 'league/champs.html', context)

def champion_average_hp(tag):
	total_hp = 0
	total_champs = 0
	for champ in Champion.objects.filter(tags__contains=tag):
		total_champs += 1
		total_hp += champ.stats['hp']
	return total_hp / total_champs

def champion_average_hpperlevel(tag):
	total_hp = 0
	total_champs = 0
	for champ in Champion.objects.filter(tags__contains=tag):
		total_champs += 1
		total_hp += champ.stats['hpperlevel']
	return total_hp / total_champs

def detail(request, champ_id):
	try:
		champ = Champion.objects.get(pk=champ_id)
	except Champion.DoesNotExist:
		raise Http404("Champion does not exist")

	base_url = "//ddragon.leagueoflegends.com/cdn/6.18.1/img/champion/"


	# Grab data for graph of health
	hp_data = []
	hp_data.append(["Level", champ.name])
	for tag in champ.tags:
		hp_data[0].append(str(tag))
	for x in range(18):
		row = [str(x+1), (champ.stats['hp'] + (x * champ.stats['hpperlevel']))]
		for tag in champ.tags:
			champ_avg_hp = champion_average_hp(tag)
			champ_avg_hpperlevel = champion_average_hpperlevel(tag)
			row.append(champ_avg_hp + x * champ_avg_hpperlevel)
		hp_data.append(row)

	from graphos.sources.simple import SimpleDataSource
	from graphos.renderers.gchart import LineChart
	champ_hp = SimpleDataSource(data=hp_data)
	hp_chart = LineChart(champ_hp)

	page_title = champ.name
	context = {
		'base_url': base_url,
		'champ': champ,
		'hp_chart': hp_chart,
		#'page_title': page_title,
	}
	return render(request, 'league/detail.html', context)


from models import Summoner
from serializers import SummonerSerializer
import json, requests, search
def search_results(request):
	query_string = ''
	found_entries = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		
		entry_query = search.get_query(query_string, ['name',])
		found_entries = Summoner.objects.filter(entry_query).order_by('-name')



		if len(found_entries) == 0:
			summoner_data = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + query_string + '?api_key=80a03926-6e55-4045-bf6f-692ec7007ca1')
			summoner_data = summoner_data.json()
			serializer = SummonerSerializer(data=summoner_data[str(query_string).lower()])
			if serializer.is_valid():
				serializer.save()
			entry_query = search.get_query(query_string, ['name',])
			found_entries = Summoner.objects.filter(entry_query).order_by('-name')

	page_title = "Search Results for '{}'".format(str(query_string))
	context = { 
				'query_string': query_string,
				'found_entries': found_entries,
				'page_title': page_title,
			}
	return render(request, 'league/search_results.html', context)


def summoner_detail(request, summoner_name):
	base_url = "//ddragon.leagueoflegends.com/cdn/6.18.1/img/champion/"
	summoner = Summoner.objects.get(name=summoner_name)
	recent_matches = summoner.matches.all().order_by('-timestamp')[:10]
	context =	{ 
				'base_url': base_url,
				'page_title': summoner_name,
				'recent_matches': recent_matches,
				'summoner': summoner,
				}
	return render(request, 'league/summoner_detail.html', context)


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

