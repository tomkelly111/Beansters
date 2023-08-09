from .models import CoffeeShopPost
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = CoffeeShopPost
        fields = ('shop', 'description', 'location', 'featured_image',)