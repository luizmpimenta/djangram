from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User (AbstractUser):
  email = models.EmailField(unique= True)
  picture = models.ImageField('Imagem de Perfil' , default = '/img/userpicture.jpeg')
  created_at = models.DateTimeField( auto_now_add=True)
  following = models.ManyToManyField('self', verbose_name='Seguindo',
                                     related_name='following_users', blank=True , symmetrical=False)
  followers = models.ManyToManyField('self', verbose_name='Seguidores',
                                     related_name='followers_users',blank=True , symmetrical=False)
  