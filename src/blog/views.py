from django.shortcuts import render , get_object_or_404
from .models import post,comment
from .forms import NewComment
from django.views.generic import CreateView



def home(request):
    context = {
        'title':'Home Page',
        'posts':post.objects.all()
    }
    return render(request , 'blog/index.html' , context)

def about(request):
    return render(request , 'blog/about.html', {'title': 'About us  '})

def post_detail(request , post_id):
    posts = get_object_or_404(post,pk=post_id)
    comments = posts.comments.filter(active = True)

    if request.method == 'POST':
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.posts = posts
            new_comment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    context = {
        'title':posts,
        'post':posts,
        'comments':comments,
        'comment_form' : comment_form,
    }

    return render(request , 'blog/detail.html', context)

class PostCreateView(CreateView):
    model = post
    fields = ['title' , 'content']
    template_name = 'blog/new_post.html'

    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)