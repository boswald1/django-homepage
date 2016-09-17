from __future__ import unicode_literals

from django.db import models
import jsonfield


class Tag(models.Model):
	tag = models.CharField(max_length=30, unique=True)

class Champion(models.Model):
	# basic info
	name = models.CharField(max_length=30)
	key = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	id = models.IntegerField(primary_key=True)
	stats = jsonfield.JSONField()
	tags = models.ManyToManyField(Tag, related_name='champion')

	# text stuff
	blurb = models.CharField(max_length=2000)
	lore = models.CharField(max_length=4500)
	allytips = jsonfield.JSONField()
	enemytips = jsonfield.JSONField()


	def __str__(self):
		return self.name

class Image(models.Model):
	champion = models.ForeignKey(Champion, related_name='image')
	full = models.CharField(max_length=50)
	group = models.CharField(max_length=50)
	sprite = models.CharField(max_length=50)
	h = models.IntegerField()
	w = models.IntegerField()
	x = models.IntegerField()
	y = models.IntegerField()

	def __str__(self):
		return self.full

class Skin(models.Model):
	champion = models.ForeignKey(Champion, related_name='skins')
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)	
	num = models.IntegerField()

	def __str__(self):
		return str("http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + str(self.champion.name) + "_" + str(self.num) + ".jpg")






	
