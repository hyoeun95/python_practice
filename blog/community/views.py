from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView
from .form import CommentForm



# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'post_list'

def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'community/post_detail.html', {'post':post})

def comment_new(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'comment_new.html', {'form': form})
