# Generated by Django 3.2.20 on 2023-08-02 16:12

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeShopPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=150)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default='Account Deleted', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='coffee_shop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
