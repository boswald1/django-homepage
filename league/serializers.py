from rest_framework import serializers
from league.models import Champion, AllyTip

class AllyTipSerializer(serializers.ModelSerializer):
	class Meta:
		model = AllyTip
		fields = ('tip',)



class ChampionSerializer(serializers.ModelSerializer):
	allytips = AllyTipSerializer(many=True)

	class Meta:
		model = Champion
		fields = ('name', 'title', 'champ_id', 'blurb', 'lore', 'key', 'allytips')
		#depth = 2

	def create(self, validated_data):
		allytips_data = validated_data.pop('allytips')
		champ = Champion.objects.create(**validated_data)
		for tip in allytips_data:
			print tip
			AllyTip.objects.create(champ_name=champ, **tip)
		return champ

	def update(self, instance, validated_data):
		print "hi"
		instance.name = validated_data.get('name', instance.name)
		instance.title = validated_data.get('title', instance.title)
		instance.champ_id = validated_data.get('champ_id', instance.champ_id)
		instance.blurb = validated_data.get('blurb', instance.blurb)
		instance.lore = validated_data.get('lore', instance.lore)
		instance.save()
		return instance



