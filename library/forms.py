from django import forms

from .models import Author, Book


class BookForm(forms.ModelForm):
	author = forms.CharField()

	def clean_author(self):
		a = self.cleaned_data['author']
		authors = []
		for x in a:
			try:
				author = Author.objects.get(name=x)
				authors.append(author)
			except Author.DoesNotExist:
				author = Author.objects.create(name=x)

		return authors

	class Meta: 
		model = Book
		fields = '__all__'




#Google Books
# key=AIzaSyChGpaRLFete7yMtuuSILmW1HZzlV6VgMY