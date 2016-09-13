import json
from league.models import Champion, Image, Tag
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = (	'full',
					'group',
					'sprite',
					'h', 'w', 'x', 'y')


class ChampionSerializer(serializers.ModelSerializer):
	image = ImageSerializer()
	allytips = serializers.JSONField()
	enemytips = serializers.JSONField()
	stats = serializers.JSONField()
	tags = serializers.JSONField()

	class Meta:
		model = Champion
		fields = (	'name', 
					'title',
					'id',
					'blurb',
					'lore',
					'key',
					'allytips',
					'enemytips',
					'stats',
					'tags',
					'image'
					)
		#depth = 2


	def create(self, validated_data):
		image_data = validated_data.pop('image')
		tags_data = validated_data.pop('tags')
		champion = Champion.objects.create(**validated_data)
		Image.objects.create(champion=champion, **image_data)
		for tag in tags_data:
			try:
				Tag.objects.create(champion=champion, **tag)
			except:
				pass
		return champion

	def update(self, instance, validated_data):
		print "hi"
		instance.name = validated_data.get('name', instance.name)
		instance.title = validated_data.get('title', instance.title)
		instance.champ_id = validated_data.get('champ_id', instance.champ_id)
		instance.blurb = validated_data.get('blurb', instance.blurb)
		instance.lore = validated_data.get('lore', instance.lore)
		instance.save()
		return instance



