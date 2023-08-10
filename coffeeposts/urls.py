from . import views
from django.urls import path
from .views import PostDetail

urlpatterns = [
    path('', views.PostList.as_view(), name='home' ),
    path('post/<str:shop>/', PostDetail.as_view(), name='post_detail'),
    path('create-coffee-shop-post/', views.create_coffee_shop_post, name='create_coffee_shop_post'),
    path('post-approval/', views.post_approval_view, name='post_approval'),
    path('edit-post/', views.edit_post_view, name="edit_post")

]