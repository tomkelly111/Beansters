from .models import CoffeeShopPost, Comment
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = CoffeeShopPost
        fields = ('shop', 'description', 'location', 'featured_image',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
    


# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('reply_body',)
