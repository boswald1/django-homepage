from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Post

# Create your views here.
def index(request):
	latest_posts = Post.objects.order_by('-pub_date')[:5]
	template = loader.get_template('blog/index.html')
	context = {
		'latest_posts': latest_posts,
	}
	return render(request, 'blog/index.html', context)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})