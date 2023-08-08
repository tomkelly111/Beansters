from . import views
from django.urls import path
from .views import PostDetail

urlpatterns = [
    path('', views.PostList.as_view(), name='home' ),
    path('post/<str:shop>/', PostDetail.as_view(), name='post_detail')
]