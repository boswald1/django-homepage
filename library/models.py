from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class BookManager(models.Manager):
	def create_book(self, front_cover, back_cover, publication_page):
		book = self.create(title=title)
		# pull info from pictures here
		return book

class Book(models.Model):
	title = models.CharField(max_length=30)
	publication_year = models.DateField()

	author = models.ForeignKey('Author', on_delete=models.CASCADE,)

	front_cover = models.ImageField(upload_to='library/static/')
	back_cover = models.ImageField(upload_to='library/static/')
	publication_page = models.ImageField(upload_to='library/static/')

	def __str__(self):
		return self.title

class Author(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __str__(self):
		name = self.first_name + " " + self.last_name
		return name