from django.shortcuts import render, redirect
from .forms import new_pet
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

def upload(request):
    form = new_pet(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('index')
    context = {
        'form':form
    }
    return render(request, 'upload.html', context)