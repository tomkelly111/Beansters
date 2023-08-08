from django.shortcuts import render, get_object_or_404  
from django.views import generic, View
from .models import CoffeeShopPost


class PostList(generic.ListView):
    model = CoffeeShopPost
    queryset = CoffeeShopPost.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

# Create your views here.
class PostDetail(View):
    def get(self, request, shop, *args, **kwargs):
        queryset = CoffeeShopPost.objects
        post = get_object_or_404(queryset, shop=shop)

        return render(
            request,
            "post_detail.html", {
                "post": post,
                "shop": shop
            }
        )

