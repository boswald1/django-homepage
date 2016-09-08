from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Champion(models.Model):
	# basic info
	name = models.CharField(max_length=30)
	title = models.CharField(max_length=30)

	blurb = models.CharField(max_length=2000)
	lore = models.CharField(max_length=2000)

	# champ statistics
	
	# champion images
