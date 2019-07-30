from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Post


class UserHasAccessToDeletePostMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request,
                       'Nao pode deletar post de outro usuario!')
        return redirect('posts:list_post')

    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['pk'])

        if not post.author == request.user:
            return self.handle_no_permission()
            return super().dispatch(self,request,*args,**kwargs)
        
        
