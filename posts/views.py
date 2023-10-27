from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView

class Blog(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name ='posts'
    paginate_by = 6

    def get_context_data(self,**kwargs):
        context = super(Blog, self).get_context_data(**kwargs)
        context["page_class"] = "blog"
        return context
    # context = {}
    # context["posts"] = Post.objects.all()
    # return render(request, 'posts/index.html', context)

def single(request, post_slug):
    context = {}
    context["post"] = get_object_or_404(Post, slug=post_slug)
    return render(request, 'posts/single.html', context)
