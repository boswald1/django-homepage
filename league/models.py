from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Champion(models.Model):
	# basic info
	name = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	champ_id = models.IntegerField(primary_key=True)

	# text stuff
	blurb = models.CharField(max_length=2000)
	lore = models.CharField(max_length=2000)



	# champ statistics
	armor = models.FloatField()
	armor_per_level = models.FloatField()
	attack_damage = models. FloatField()
	attack_damage_per_level = models.FloatField()
	attack_range = models.FloatField()
	attack_speed_offset = models.FloatField()
	attack_speed_per_level = models.FloatField()
	crit = models.FloatField()
	crit_per_level = models.FloatField()
	hp = models.FloatField()
	hp_per_level = models.FloatField()
	hp_regen = models.FloatField()
	hp_regen_per_level = models.FloatField()
	movespeed = models.FloatField()
	mana = models.FloatField()
	mana_per_level = models.FloatField()
	mana_regen = models.FloatField()
	mana_regen_per_level = models.FloatField()
	spell_block = models.FloatField()
	spell_block_per_level = models.FloatField()

	# champion abilities

	def __str__(self):
		return self.name

class image(models.Model):
	# Stores information about image resources for champions
	full = models.CharField(max_length=50)
	group = models.CharField(max_length=50)
	sprite = models.CharField(max_length=50)

	h = models.IntegerField()
	w = models.IntegerField()
	x = models.IntegerField()
	y = models.IntegerField()

	
class info(models.Model):
	# 
	attack_rating = models.IntegerField()
	defense_rating = models.IntegerField()
	difficulty_rating = models.IntegerField()
	magic_rating = models.IntegerField()

