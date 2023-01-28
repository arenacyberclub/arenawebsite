# Generated by Django 3.2.16 on 2023-01-20 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arena_cyber_sport', '0002_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='game_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='games/'),
            preserve_default=False,
        ),
    ]
