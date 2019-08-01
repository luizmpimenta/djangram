from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(
        'users.User', verbose_name='Author', related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Imagem', upload_to='posts/')
    description = models.CharField(max_length=256, verbose_name='Descrição')
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True)
    modified_at = models.DateTimeField(
        verbose_name='Modificado em', auto_now=True)

    def __str__(self):
        return f'Post{self.pk} | Author {self.author} | Created at {self.created_at}'

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

class Comment(models.Model):
    autor = models.ForeignKey("users.User", verbose_name='Autor',
                                  related_name='commentsFromUser', on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', verbose_name='Post',
                                 related_name='commentsFromPost', on_delete=models.CASCADE)
    text = models.TextField('Texto')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
        
    def __str__(self):
        return f'Comment {self.pk} | Author {self.autor} | Post {self.post.pk} | Created at {self.created_at} '
    
    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentários'
        
