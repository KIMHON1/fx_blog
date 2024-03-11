from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


