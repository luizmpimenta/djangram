from django.urls import path
from .views import UserLoginView , UserLogoutView , UserDetailView ,UserSignupView,UserUpdateView,UserFollowView


app_name = 'users'

urlpatterns = [
    #1- rota , 2 - view-as.view() ,3 nome da view 
    path('login/', UserLoginView.as_view(),name='login_user' ),
    path('logout/',UserLogoutView.as_view(),name='logout_user'),
    path('perfil/<int:pk>/',UserDetailView.as_view(),name='detail_user'),
    path('signup/',UserSignupView.as_view(),name='signup'),
    path('editar_perfil/<int:pk>/',UserUpdateView.as_view(),name='update_user'),
    path('seguir/<int:pk>/',UserFollowView.as_view(), name='follow_user'),
    
]
