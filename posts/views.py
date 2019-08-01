from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from posts.forms import PostCreateForm
from .mixins import UserHasAccessToDeletePostMixin
from posts.models import Post


class PostListView(LoginRequiredMixin , generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/list_post.html'
    ordering = ['-created_at',]

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts:list_post')
    
    def get_initial(self):
        return {
            'user': self.request.user,
        }

    def form_valid(self, form):
        messages.success(self.request, 'Você compartilhou um novo post! Confira abaixo.')
        return super().form_valid(form)
    
class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/detail_post.html'  

class PostDeleteView(UserHasAccessToDeletePostMixin,generic.DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/delete_post.html'
    def get_success_url(self):
        import ipdb; ipdb.set_trace()
        return reverse_lazy('users:detail_user', args=[self.object.pk])
   
        
    