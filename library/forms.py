from django import forms

from .models import Author, Book

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = ['name']

class BookForm(forms.ModelForm):
	author = forms.CharField()

	def clean_author(self):
		a = self.cleaned_data['author']

		try:
			author = Author.objects.get(name=a)
		except Author.DoesNotExist:
			author = Author.objects.create(name=a)

		return author

	class Meta: 
		model = Book
		fields = ['title', 'publication_year', 'author', 'front_cover', 'back_cover', 'publication_page']
