from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import BookForm
from .models import Book

		
def add_book(request):
	page_title = "Add a New Book"

	if request.method == 'POST':
		book_form = BookForm(request.POST or None, request.FILES or None)
		if book_form.is_valid():
			# process data in book_form.cleaned_data here
			book_form.save()
			return HttpResponseRedirect('/library/')
	else:
		book_form = BookForm()


	context = {
		'book_form': book_form,
		'page_title': page_title,
	}
	return render(request, 'library/add_book.html', context)

def index(request):
	book_list = Book.objects.order_by('-title')

	page_title = "Library Homepage"

	context = {
		'book_list': book_list,
		'page_title': page_title,
	}
	return render(request, 'library/index.html', context)


def detail(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
	except Book.DoesNotExist:
		raise Http404("Book does not exist")
	page_title = book.title
	context = {
		'book': book,
		'page_title': page_title,
	}
	return render(request, 'library/detail.html', context)