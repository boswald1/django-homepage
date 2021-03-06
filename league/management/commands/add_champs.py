import json
import urllib2
import requests
from django.core.management.base import BaseCommand
from league.models import Champion
from league.serializers import ChampionSerializer

class Command(BaseCommand):
	args = ''
	help = 'update champion information using league API'

	def _get_data(self):
		f = open('league/management/commands/data/champdata.json', 'w')
		data = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=80a03926-6e55-4045-bf6f-692ec7007ca1')
		data = data.json()
		json.dump(data['data'], f, sort_keys = True, indent = 4)
		f.close()

		f = open('league/management/commands/data/champkeys.json', 'w')
		json.dump(data['keys'], f, sort_keys = True, indent = 4)
		f.close()


	def _deserializeJSON(self):
		with open('league/management/commands/data/champkeys.json') as f:
			champions = json.load(f)
			champkeys = champions.keys()

		with open('league/management/commands/data/champdata.json', 'r') as f:
			data = json.load(f)

 			for key in champkeys:
	 			serializer = ChampionSerializer(data=data[ champions[str(key)] ])
	 			if serializer.is_valid():
	 				print "Adding " + champions[str(key)]
		 			serializer.save()
	 			else:
	 				print serializer.errors



	def handle(self, *args, **options):
		#self._get_data()
		self._deserializeJSON()
