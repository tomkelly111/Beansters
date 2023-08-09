# Generated by Django 3.2.20 on 2023-08-09 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffeeposts', '0005_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default='Account Deleted', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='user_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
