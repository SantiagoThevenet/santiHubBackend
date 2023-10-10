from django.contrib import admin

from .models import PostAttachment, Post


admin.site.register(Post)
admin.site.register(PostAttachment)