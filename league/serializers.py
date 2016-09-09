from rest_framework import serializers
from league.models import Champion

class ChampionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Champion
		fields = ('name', 'title', 'champ_id', 'blurb', 'lore')