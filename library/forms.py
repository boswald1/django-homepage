from django.forms import ModelForm

from .models import Book

class BookForm(ModelForm):
	class Meta: 
		model = Book
		fields = ['front_cover', 'back_cover', 'publication_page']