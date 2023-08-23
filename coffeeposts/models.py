from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class CoffeeShopPost(models.Model):
    shop = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150)
    review = models.CharField(max_length=600)
    author = models.ForeignKey(User,
                               on_delete=models.SET_DEFAULT,
                               default='Account Deleted',
                               related_name='coffee_shop')
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False)
    location = models.CharField(max_length=150, default='')
    stars = (
        (0, "N/A"),
        (1, "1 Star = Do not reccomend"),
        (2, "2 Star = Would visit if no other options"),
        (3, "3 Star = Not bad if you need a fix"),
        (4, "4 Star = They know what they are doing"),
        (5, "5 Star = Must try!")
        )
    rating = models.IntegerField(choices=stars, default=0)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.shop


class Comment(models.Model):
    post = models.ForeignKey(CoffeeShopPost,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    stars = (
        (0, "N/A"),
        (1, "1 Star = Do not reccomend"),
        (2, "2 Star = Would visit if no other options"),
        (3, "3 Star = Not bad if you need a fix"),
        (4, "4 Star = They know what they are doing"),
        (5, "5 Star = Must try!")
        )
    rating = models.IntegerField(choices=stars, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.body
