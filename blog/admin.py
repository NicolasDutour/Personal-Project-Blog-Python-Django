from django.contrib import admin
from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_on', 'last_modified')
    list_display_links = ('id', 'title', 'body')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'body', 'created_on', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
