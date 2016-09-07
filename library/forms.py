from django.forms import ModelForm

from .models import Book

class BookForm(ModelForm):
	class Meta: 
		model = Book
		fields = ['title', 'publication_year', 'author', 'front_cover', 'back_cover', 'publication_page']