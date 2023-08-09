from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.


class CoffeeShopPost(models.Model):
    shop = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Account Deleted', related_name='coffee_shop')
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False)
    location = models.CharField(max_length=150, default='')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.shop


class Comment(models.Model):
    post = models.ForeignKey(CoffeeShopPost, on_delete=models.CASCADE, related_name='comments')
    comm_name = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1, related_name='user_review')
    name = models.CharField(max_length=80, default="DEFAULT")
    approved = models.BooleanField(default=False)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    body = models.TextField(max_length=500)
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.comm_name



# class Reply(models.Model):
#     comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE,related_name='replies')
#     reply_body = models.TextField(max_length=500)
#     author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Account Deleted')
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return "reply to " + str(self.comment_name.comm_name)