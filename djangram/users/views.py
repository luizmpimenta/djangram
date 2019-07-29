from django.shortcuts import render
from .mixins import UserHasAccessToDetailMixin , LoginRequiredMixin
from django.contrib.auth.views import LoginView , LogoutView 
from django.views import generic
from .models import User
from django.urls import reverse_lazy
from .forms import UserSignupForm
# Create your views here.

class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LoginRequiredMixin,LogoutView):
    pass    


class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'users/detail_user.html'

class UserSignupView(generic.CreateView):
    model = User
    form_class = UserSignupForm
    template_name = 'users/signup_user.html'
    success_url = reverse_lazy('users:login_user')

class UserUpdateView(UserHasAccessToDetailMixin,generic.UpdateView):
    model = User
    fields = [ 'username' , 'picture' ]
    template_name = 'users/update_user.html'
    
    def get_success_url(self):
        return reverse_lazy('users:detail_user', args=[self.object.pk])
        
