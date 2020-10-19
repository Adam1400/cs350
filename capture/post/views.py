from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.forms import ModelForm
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
from django.contrib.auth.decorators import login_required

# load templates
def index(request):
    context = { 'posts': Post.objects.all() }
    return render(request, 'post/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'
    ordering = ['-post_date'] # order of posts (newest first)

class PostDetailView(DetailView):
    model = Post

@login_required  
def post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        form.instance.user = request.user

        if form.is_valid():
            form.save()
            indexcontext = { 'posts': Post.objects.all() }
            return HttpResponseRedirect(reverse('capture-home'))

    
    context = {'form':form, 'title': 'Post'}
    return render(request, 'post/post.html', context )

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['comment', 'content']

        
        
            
    


