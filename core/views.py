from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comments
from .forms import CommentForm
from django.db.models import Q 
from django.http import HttpResponse

def index(request):
    # only display active posts on the frontpage
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'core/index.html', {'posts': posts})


def search(request):
    query = request.GET.get('query', '')
    # only get active posts that match the query
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query))

    return render(request, 'core/search.html', {'posts': posts, 'query': query})



def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'/details/{post.slug}')

    form = CommentForm()
    return render(request, 'core/details.html', {'post': post, 'form': form})


def get_category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'core/category.html', {'category': category, 'posts': posts})


def robot_texts(request):
    text = [
        'User-Agent: *',
        'Disallow: /admin/',
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")