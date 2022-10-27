from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# Create your views here.
from .forms import CommentForm
from .models import Post

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'djangoblog/detail.html', {'post': post, 'form': form})

def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title_icontains=query) | Q(intro_icontains=query) | Q(body_icontains=query))

    return render(request, 'djangoblog/search.html', {'posts': posts, 'query': query})
