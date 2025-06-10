from django.shortcuts import render,redirect
from sections.models import Category, Post
from sections.forms import CommentForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def frontpageView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'frontpage.html', context)

def detailView(request, slug, pk):
    post=Post.objects.get(slug=slug, pk=pk)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post=post
            obj.save()
            return redirect('detail_url',slug=post.slug, pk=post.pk)
    else:
        form=CommentForm()

    context={
        'post_detail':post,
        'form_detail':form,
        'id':pk
    }
    return render(request,'detail.html', context)

def categoryView(request, slug):
    category=Category.objects.get(slug=slug)
    context={
        'category_pair':category
    }
    return render(request,'category.html', context)

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
