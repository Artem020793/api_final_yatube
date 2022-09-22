# Generated by Django 3.2.15 on 2022-09-21 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_post_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.CASCADE, related_name='following', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(default=12345, on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_follow'),
        ),
    ]
