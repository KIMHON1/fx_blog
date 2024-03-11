from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import ContactForm
# Create your views here.

def post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'post_detail.html', {'post': post})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, redirect to a success page
            return redirect('/blog')

    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})