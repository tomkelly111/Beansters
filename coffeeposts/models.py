from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.


class CoffeeShopPost(models.Model):
    shop = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default='Account Deleted', related_name='coffee_shop')
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.shop
        