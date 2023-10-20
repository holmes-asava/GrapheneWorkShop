from django.contrib import admin

from post_manager.models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)
