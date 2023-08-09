from django.contrib import admin
from .models import CoffeeShopPost, Comment


@admin.register(CoffeeShopPost)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['shop']
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('post', 'comm_name', 'author')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# @admin.register(Reply)
# class CommentAdmin(admin.ModelAdmin):
#     search_fields = ('comment_name', 'author',)
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(approved=True)
