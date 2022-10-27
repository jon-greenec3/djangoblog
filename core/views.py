from django.shortcuts import render

from djangoblog.models import Post
# Create your views here.

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'core/frontpage.html', {'posts': posts})
