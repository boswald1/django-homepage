from __future__ import unicode_literals

from django.db import models
import jsonfield




class Champion(models.Model):
	# basic info
	name = models.CharField(max_length=30)
	key = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	id = models.IntegerField(primary_key=True)
	stats = jsonfield.JSONField()

	# text stuff
	blurb = models.CharField(max_length=2000)
	lore = models.CharField(max_length=4500)
	tags = jsonfield.JSONField()
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
		return str("http://ddragon.leagueoflegends.com/cdn/img/champion/splash/" + str(self.champion.key) + "_" + str(self.num) + ".jpg")






class Summoner(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50, unique=True)
	#matches = models.ForeignKey(Match, many=True, blank=True)
	profileIconId = models.IntegerField()
	revisionDate = models.BigIntegerField()
	summonerLevel = models.IntegerField()

	def __str__(self):
		return self.name


class Match(models.Model):
	champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
	summoner = models.ForeignKey(Summoner, related_name='matches', on_delete=models.CASCADE)
	
	timestamp = models.BigIntegerField()
	matchId = models.BigIntegerField(primary_key=True)


	# These fields should also be choices
	queue = models.CharField(max_length=50)
	season = models.CharField(max_length=50)
	role = models.CharField(max_length=25)
	platformId = models.CharField(max_length=10)

	# lane options
	MID = 'MID'
	TOP = 'TOP'
	BOTTOM = 'BOT'
	SUPP = 'SUP'
	JUNGLE = 'JNG'
	lane_choices = (
			(MID, 'Middle'),
			(TOP, 'Top'),
			(BOTTOM, 'Marksman'),
			(SUPP, 'Support'),
			(JUNGLE, 'Jungle'),
		)
	lane = models.CharField(
			max_length=3,
			choices = lane_choices,
		)

	# region options
	NORTH_AMERICA = 'NA'
	EU_WEST = 'EUW'
	EU_NORDIC_EAST = 'EUNE'
	LATIN_AMERICA_NORTH = 'LAN'
	LATIN_AMERICA_SOUTH = 'LAS'
	BRAZIL = 'BR'
	JAPAN = 'JP'
	RUSSIA = 'RU'
	TURKEY = 'TR'
	OCEANA = 'OCE'
	REP_OF_KOREA = 'KR'
	REGION_CHOICES = (
			(NORTH_AMERICA, 'North America'),
			(EU_WEST, 'Europe West'),
			(EU_NORDIC_EAST, 'Europe Nordic and East'),
			(LATIN_AMERICA_NORTH, 'Latin America North'),
			(LATIN_AMERICA_SOUTH, 'Latin America South'),
			(BRAZIL, 'Brazil'),
			(JAPAN, 'Japan'),
			(RUSSIA, 'Russia'),
			(TURKEY, 'Turkey'),
			(OCEANA, 'Oceana'),
			(REP_OF_KOREA, 'Korea'),
		)
	region = models.CharField(
			max_length=2,
			choices=REGION_CHOICES,
			default='NORTH_AMERICA'
		)








	
