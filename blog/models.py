from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=100)

class Post(models.Model):
	title = models.CharField(max_length=100)
	post_body = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
