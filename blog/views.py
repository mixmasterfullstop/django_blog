from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request,'blog/home.html', {'posts':posts,'title':'home'})

def detail(request, post_id):
     post = get_object_or_404(Post, pk=post_id)

     return render(request,'blog/detail.html',{'post':post, 'title':'detail'})

def about(request):
    return render(request, 'blog/about.html',{'title':'about',})