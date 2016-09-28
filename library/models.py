from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Book(models.Model):
	title = models.CharField(max_length=30)
	publication_year = models.IntegerField()

	author = models.ForeignKey('Author', on_delete=models.CASCADE,)

	front_cover = models.ImageField(upload_to='static/books/')
	back_cover = models.ImageField(upload_to='static/books/')
	publication_page = models.ImageField(upload_to='static/books/')

	def __str__(self):
		return self.title



class Author(models.Model):
	name = models.CharField(max_length=100)	

	def __str__(self):
		name = self.name
		return name