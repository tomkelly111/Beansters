from django.shortcuts import render, get_object_or_404, redirect  
from django.views import generic, View
from .models import CoffeeShopPost, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages


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
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
                request,
                "post_detail.html", {
                    "post": post,
                    "comments": comments,
                    "comment_form": CommentForm()
                }
            )

    def post(self, request, shop, *args, **kwargs):
        queryset = CoffeeShopPost.objects
        post = get_object_or_404(queryset, shop=shop)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "post_detail.html", {
                "post": post,
                "commented": True,
                "comments": comments,
                "comment_form": CommentForm()
            }
        )


    
    
def post_approval_view(request):
    return render(request, 'post_approval.html')

def edit_post_view(request):
    return render(request, 'edit_post.html') # maybe can be deleted

def create_coffee_shop_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.approved = False
            post.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully added a Coffee Shop. Your post will be visible once it is approved')
            return redirect('post_approval') 
    else:
        form = PostForm()

    return render(request, 'new_post.html', {'form': form})

def edit_post(request, post_id):
    post_to_edit = get_object_or_404(CoffeeShopPost, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post_to_edit)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.approved = False
            post.save()
            return redirect('post_approval')
    form = PostForm(instance=post_to_edit)
    return render(request, 'edit_post.html', {'form': form})


def post_deleted(request):
    return render(request, 'post_deleted.html')

def delete_post(request, post_id):
    post = get_object_or_404(CoffeeShopPost, id=post_id)
    if post.author == request.user:
        post.delete()
        return redirect('post_deleted')

