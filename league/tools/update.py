import json
import urllib2
import requests


def refresh_data():
	f = open('/Users/boswald/Sites/gcloudsite/appengine-django-skeleton/league/tools/data/champdata.json', 'w')
	data = requests.get('https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=all&api_key=80a03926-6e55-4045-bf6f-692ec7007ca1')
	data = data.json()
	json.dump(data['data'], f, sort_keys = True, indent = 4)
	f.close()

	f = open('/Users/boswald/Sites/gcloudsite/appengine-django-skeleton/league/tools/data/champkeys.json', 'w')
	json.dump(data['keys'], f, sort_keys = True, indent = 4)
	f.close()

def update_champs():
	with open('/Users/boswald/Sites/gcloudsite/appengine-django-skeleton/league/tools/data/champkeys.json') as f:
		champions = json.load(f)
		champkeys = champions.keys()
		#print champions
		#print champkeys

	with open('/Users/boswald/Sites/gcloudsite/appengine-django-skeleton/league/tools/data/champdata.json') as f:
		data = json.load(f)


	import os
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

	import django
	django.setup()
	from league.models import AllyTip, Champion


	for champ in champkeys:
		entry = data[ champions[str(champ)] ]

		atips = []
		for atip in entry['allytips']:
			atipinstance = AllyTip.objects.create(tip=atip)
			atipinstance.save()
			atips.append(atipinstance.id)
		

		champion_instance = Champion(
			name=entry['name'], 
			title=entry['title'],
			champ_id=entry['id'],
			blurb=entry['blurb'],
			lore=entry['lore'],
		)
		champion_instance.save()

		print atips
		champion_instance.allytips = (atips)
'''	
refresh_data()
update_champs()


'''
with open('/Users/boswald/Sites/gcloudsite/appengine-django-skeleton/league/tools/data/champkeys.json') as f:
	champions = json.load(f)
	champkeys = champions.keys()
	#print champions
	#print champkeys

with open('/Users/boswald/Sites/gcloudsite/appengine-django-skeleton/league/tools/data/champdata.json') as f:
	data = json.load(f)

lorelengths = []
for key in champkeys:
	lorelengths.append(len(data[champions[str(key)]]['allytips']))

print max(lorelengths)

