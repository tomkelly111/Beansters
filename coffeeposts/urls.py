from . import views
from django.urls import path
from .views import PostDetail, edit_post, delete_post, search_shops

urlpatterns = [
    path('', views.PostList.as_view(), name='home' ),
    path('post/<str:shop>/', PostDetail.as_view(), name='post_detail'),
    path('create-coffee-shop-post/', views.create_coffee_shop_post, name='create_coffee_shop_post'),
    path('post-approval/', views.post_approval_view, name='post_approval'),
    path('edit/<post_id>', edit_post, name='edit_post'),
    path('delete/<post_id>', delete_post, name='delete_post'),
    path('search_shops>', search_shops, name='search_shops')


]