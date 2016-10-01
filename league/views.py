from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Champion

API_KEY="80a03926-6e55-4045-bf6f-692ec7007ca1"

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



from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
def initialize_stat_charts(champ):
	# Grab data for graphs
	stat_charts = []

	for stat in champ.stats:
		if stat[-8:] == "perlevel":
			continue	

		elif stat == "attackspeedoffset" or stat == "attackrange" or stat == "movespeed":
			continue
		else:
			stat_data = []
			stat_data.append(["Level", champ.name])
			for tag in champ.tags:
				stat_data[0].append(str(tag))
			stat_data[0].append('All Champs')
			for x in range(18):
				row = [str(x+1), (champ.stats[stat] + (x * champ.stats[stat + 'perlevel']))]
				for tag in champ.tags:
					champ_avg_hp = champion_average_hp(tag)
					champ_avg_hpperlevel = champion_average_hpperlevel(tag)
					row.append(champ_avg_hp + x * champ_avg_hpperlevel)
				stat_data.append(row)

				champ_avg_hp = champion_average_hp('')
				champ_avg_hpperlevel = champion_average_hpperlevel('')
				row.append(champ_avg_hp + x * champ_avg_hpperlevel)

			champ_stat = SimpleDataSource(data=stat_data)
			stat_chart = LineChart(champ_stat, options={'title': stat})
			stat_charts.append(stat_chart)
	return stat_charts



def detail(request, champ_id):
	try:
		champ = Champion.objects.get(pk=champ_id)
	except Champion.DoesNotExist:
		raise Http404("Champion does not exist")

	base_url = "//ddragon.leagueoflegends.com/cdn/6.18.1/img/champion/"


	stat_charts = initialize_stat_charts(champ)	
	page_title = champ.name
	context = {
		'base_url': base_url,
		'champ': champ,
		'stat_charts': stat_charts,
		#'page_title': page_title,
	}
	return render(request, 'league/detail.html', context)


from models import Summoner
from serializers import SummonerSerializer
import json, requests, search
def search_results(request):
	query_string = ''
	found_summoners = None
	found_champs = None
	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		
		entry_query = search.get_query(query_string, ['name',])
		found_summoners = Summoner.objects.filter(entry_query).order_by('-name')
		found_champs = Champion.objects.filter(entry_query).order_by('-name')


		if len(found_summoners) == 0 and len(found_champs) == 0:
			summoner_data = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + query_string + '?api_key=' + API_KEY)
			summoner_data = summoner_data.json()
			serializer = SummonerSerializer(data=summoner_data[str(query_string).lower()])
			if serializer.is_valid():
				serializer.save()
			entry_query = search.get_query(query_string, ['name',])
			found_summoners = Summoner.objects.filter(entry_query).order_by('-name')

	page_title = "Search Results for '{}'".format(str(query_string))
	context = { 
				'query_string': query_string,
				'found_summoners': found_summoners,
				'found_champs': found_champs,
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

