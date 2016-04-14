from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'diary/index.html',
        {   'post':post,

        })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'diary/post_detail.html',
        {
        'post':post,
        })