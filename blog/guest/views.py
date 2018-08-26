from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'post_list'

def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'community/post_detail.html', {'post':post})