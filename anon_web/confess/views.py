from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post


def home(request):
    context = {
        'items': Post.objects.all().order_by("-date_posted")
    }
    return render(request, 'confess/home.html', context)


def story(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.all().order_by('-date_posted')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('confess-story', pk=post.id)
    else:
        form = CommentForm()

    context = {
        'item': post,
        'comments': comments,
        'form': form
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