from django.shortcuts import render, get_object_or_404, redirect  
from django.views import generic, View
from .models import CoffeeShopPost
from .forms import PostForm

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
    
def post_approval_view(request):
    return render(request, 'post_approval.html')

def create_coffee_shop_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # Create the object but don't save it yet
            post.author = request.user  # Set the author to the currently logged-in user
            post.approved = False
            post.save()
            return redirect('post_approval') 
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})
