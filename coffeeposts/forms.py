from .models import CoffeeShopPost, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = CoffeeShopPost
        fields = ('shop', 'description',
                  'review', 'location', 'featured_image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
