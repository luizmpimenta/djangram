from django.contrib import admin

from posts.models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.site_header = 'Djangram'
admin.site.index_title = 'Admin Djangram'