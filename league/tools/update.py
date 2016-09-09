import json
import urllib2
import requests


def refresh_data():
	f = open('data/champdata.json', 'w')
	data = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=80a03926-6e55-4045-bf6f-692ec7007ca1')
	data = data.json()
	json.dump(data['data'], f, sort_keys = True, indent = 4)
	f.close()

	f = open('data/champkeys.json', 'w')
	json.dump(data['keys'], f, sort_keys = True, indent = 4)
	f.close()

refresh_data()