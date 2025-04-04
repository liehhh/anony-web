from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def home(request):
    context = {
        'items': Post.objects.all().order_by("-date_posted")
    }
    return render(request, 'confess/home.html', context)

def story(request, pk):
    context = {
        'item': Post.objects.get(id=pk)
    }
    return render(request, 'confess/story.html', context)

def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('confess-story', pk=post.pk)
    form = PostForm(request.POST)
    return render(request, 'confess/create.html', {"form": form})

def search_results(request):
    query = request.GET.get("q", "")
    posts = Post.objects.all().order_by("-date_posted")
    filtered_posts = [post for post in posts if query.lower() in post.title.lower() and query is not ""]

    return render(request, 'confess/search_results.html', {"query": query, "posts": filtered_posts})