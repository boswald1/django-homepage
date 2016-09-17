import json
from league.models import Champion, Image, Tag, Skin
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = (	'full',
					'group',
					'sprite',
					'h', 'w', 'x', 'y')

class SkinSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skin
		fields = (	'id',
					'name',
					'num'
				)


class ChampionSerializer(serializers.ModelSerializer):
	image = ImageSerializer()
	skins = SkinSerializer(many=True)
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
					'image',
					'skins'
					)
		#depth = 2


	def create(self, validated_data):
		# Pop off data which must be serialized seperately
		image_data = validated_data.pop('image')
		tags_data = validated_data.pop('tags')
		skin_data = validated_data.pop('skins')

		# create model instances for singular objects
		champion = Champion.objects.create(**validated_data)
		Image.objects.create(champion=champion, **image_data)

		# create model instances for multiple objects
		for tag in tags_data:
			try:
				Tag.objects.create(champion=champion, **tag)
			except:
				pass

		for skin in skin_data:
			try:
				Skin.objects.create(champion=champion, **skin)
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



