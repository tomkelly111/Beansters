from django.shortcuts import render
from django.views import generic
from .models import CoffeeShopPost


class PostList(generic.ListView):
    model = CoffeeShopPost
    queryset = CoffeeShopPost.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

# Create your views here.
