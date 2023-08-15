from . import views
from django.urls import path
from .views import PostDetail

urlpatterns = [
    path('', views.PostList.as_view(), name='home' ),
    path('post/<str:shop>/', PostDetail.as_view(), name='post_detail'),
    path('create-coffee-shop-post/', views.create_coffee_shop_post, name='create_coffee_shop_post'),
    path('edit/<post_id>', views.edit_post, name='edit_post'),
    path('delete/<post_id>', views.delete_post, name='delete_post'),
    path('search_shops/', views.search_shops, name='search_shops')


]