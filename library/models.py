from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class Book(models.Model):
	title = models.CharField(max_length=30)
	publication_year = models.IntegerField(blank=True, null=True)
	copyright = models.IntegerField(blank=True, null=True)
	edition = models.IntegerField(blank=True, null=True)
	printing = models.IntegerField(blank=True, null=True)

	hardcover = models.BooleanField()

	'''
	types_of_media = (
		(NOVEL, 'Novel'),
		(SS, 'Short Stories'),
		(ESSAYS, 'Essays'),
		(MAG, 'Magazines'),
		(AUTOBIO, 'Autobiography'),
		(PROSE, 'Collection of Prose'),
		(ARTICLES, 'Collection of Articles'),
		(TRAN, 'Court Transcript'),
		(CHRIST, 'Christian Resource'),
		(CART, 'Collection of Cartoons'),
	)
	'''

	media_type = models.CharField(max_length=25,blank=True)

	notes = models.CharField(max_length=500, blank=True)
	worth = models.CharField(max_length=500, blank=True)

	author = models.ManyToManyField('Author')

	editor = models.CharField(max_length=100, blank=True)
	translator = models.CharField(max_length=100, blank=True) 
	illustrator = models.CharField(max_length=100, blank=True)


	front_cover = models.ImageField(upload_to='/static/books/', blank=True)
	back_cover = models.ImageField(upload_to='/static/books/', blank=True)
	publication_page = models.ImageField(upload_to='/static/books/', blank=True)

	def __str__(self):
		return self.title



class Author(models.Model):
	name = models.CharField(max_length=100)	

	def __str__(self):
		name = self.name
		return name