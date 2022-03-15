from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import Post
from .serializer import JsonPost
from rest_framework import viewsets
import requests
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )

# Create your views here.
class Post_List(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = JsonPost

# -------use json in your website-------
def get_data(request):
    url='https://azizkra.pythonanywhere.com/postJS'
    data=requests.get(url).json()
    print('info: '+str(data[0]))
    return render(request,'blog/data.html',{data:data})
    
    

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10 #count the post
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10 #count the post
    
    #to show the Posts of user when click in link username
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

   



class PostDetailView(DetailView):
    model = Post




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form): #to valid user 
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        
        
      
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'# whene click yes delete send me to home page
    
    def test_func(self): # لتحقق اذا كان بلفعل المستخدم صاحب المنشور للتعديل عليه
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

  
def about(request):
    return render(request, "blog/about.html", {"title": "About"})



