from django.contrib import admin
from .models import CoffeeShopPost


@admin.register(CoffeeShopPost)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['shop']
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True)

# Register your models here.
