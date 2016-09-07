from django.http import Http404
from django.shortcuts import render

from .forms import BookForm
from .models import Book

def add_book(request):
	if request.method == 'POST':
		book_form = BookForm(request.POST)
		if book_form.is_valid():
			# process data in book_form.cleaned_data here
			return HttpResponseRedirect('/library/')
	else:
		book_form = BookForm()

	context = {'book_form': book_form }
	return render(request, 'library/add_book.html', context)

def index(request):
	book_list = Book.objects.order_by('-title')
	context = {'book_list': book_list }
	return render(request, 'library/index.html', context)


def detail(request, book_id):
	try:
		book = Book.objects.get(pk=book_id)
	except Book.DoesNotExist:
		raise Http404("Question does not exist")	
	return render(request, 'library/detail.html', {'book': book})