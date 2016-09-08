from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
	latest_posts = Post.objects.order_by('-pub_date')[:5]
	page_title = "Blog Home"

	context = {
		'page_title': page_title,
		'latest_posts': latest_posts,
	}
	return render(request, 'blog/index.html', context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	page_title = post.title

	context = {
		'post': post,
		'page_title': page_title,
	}
	return render(request, 'blog/post_detail.html', context)