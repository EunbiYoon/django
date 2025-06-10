from django.shortcuts import render
from sections.models import Post

# Create your views here.
def homeView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'home.html', context)