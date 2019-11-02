from django.shortcuts import render, redirect
from .forms import new_pet, vote_pet
from .models import Post

# Create your views here.
def index(request):
    posts = reversed(sorted(Post.objects.all().order_by(), key=lambda t: t.votes))
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

def vote(request, pet):
    form = vote_pet(request.POST or None)
    post = Post.objects.get(pk=pet)
    if form.is_valid():
        vote = form.save(commit=False)

        vote.photo_id = post

        vote.save()
        return redirect('index')
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'vote.html', context)