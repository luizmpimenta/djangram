from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('users.User',verbose_name= 'Author' ,related_name='posts',on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagem',upload_to='posts/')
    description = models.CharField(max_length=256, verbose_name='Descrição')
    created_at = models.DateTimeField(verbose_name='Criado em',auto_now_add=True)
    modified_at = models.DateTimeField( verbose_name='Modificado em',auto_now=True)
    
    def __str__(self):
        return f'Post{self.pk} | Author {self.author} | Created at {self.created_at}'
    
    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
    
    
