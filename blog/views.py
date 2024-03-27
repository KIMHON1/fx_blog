from django.shortcuts import render, redirect,get_object_or_404
from .models import BlogPost
from .forms import ContactForm
# Create your views here.

from django.shortcuts import render

def post_list(request):
    posts = BlogPost.objects.order_by('-created_at')[:4]
    return render(request, 'index.html', {'posts': posts})
    # posts = BlogPost.objects.all()
    # return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    next_post = BlogPost.objects.filter(created_at__gt=post.created_at).exclude(id=post_id).order_by('created_at').first()
   
    return render(request, 'post_detail.html', {'post': post,'next_post': next_post})


def confirmation(request):
    return render(request, 'confirmations.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, redirect to a success page
            return redirect('confirmation')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})


