from django.shortcuts import render
from .mixins import UserHasAccessToDetailMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic

from .models import User
from django.urls import reverse_lazy
from .forms import UserSignupForm
from .helpers import send_confirm_user_signup_email
#from django.core.mail import send_mail
# Create your views here.


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/detail_user.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request_user = User.objects.get(pk=self.request.user.pk)
        follow_user = kwargs['object']
        context['request_user_has_followed'] = request_user.following.filter(pk=follow_user.pk)
        return context


class UserSignupView(generic.CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'users/signup_user.html'
    success_url = reverse_lazy('users:login_user')

    def form_valid(self, form):
        self.object = form.save()
        send_confirm_user_signup_email(self.object)
        return super().form_valid(form)


class UserUpdateView(UserHasAccessToDetailMixin, generic.UpdateView):
    model = User
    fields = ['username', 'picture']
    template_name = 'users/update_user.html'

    def get_success_url(self):
        return reverse_lazy('users:detail_user', args=[self.object.pk])

class UserFollowView(generic.RedirectView):
    def get_redirect_url(self,*args, **kwargs):
        # usuario logado
        request_user = User.objects.get(pk=self.request.user.pk)  
        # usuario do perfil a ser seguido ou deixar de seguir  
        following_user = User.objects.get(pk=kwargs['pk']) 
        
        #analisar se o perfil ja esta sendo seguido 
        request_user_has_followed = request_user.following.filter(pk= following_user.pk)
        
        if not request_user_has_followed:
            #seguindo o perfil 
            request_user.following.add(following_user)
            #adicionando a lista de seguidores do perfil , o usuario logado 
            following_user.followers.add(request_user)  
        else:
            #deixando de seguir o perfil caso ja o siga
            request_user.following.remove(following_user)
            #removendo o perfil logado da lista de seguidores do perfil selecionado
            following_user.followers.remove(request_user)     
        
        return reverse_lazy('users:detail_user', args=[following_user.pk])