from __future__ import unicode_literals

from django.db import models



class Champion(models.Model):
	# basic info
	name = models.CharField(max_length=30)
	key = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	champ_id = models.IntegerField(primary_key=True)

	# text stuff
	blurb = models.CharField(max_length=2000)
	lore = models.CharField(max_length=4500)

	def __str__(self):
		return self.name

class AllyTip(models.Model):
	champ_name = models.ForeignKey(Champion, related_name='allytips')
	tip = models.CharField(max_length=250)

	def __str__(self):
		return self.tip




	
