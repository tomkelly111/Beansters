from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coffeeposts.urls'), name='coffeeposts_url;'),
    path('accounts/', include('allauth.urls')),
]
