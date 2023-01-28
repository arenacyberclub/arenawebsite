# Generated by Django 3.2.16 on 2023-01-22 13:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arena_cyber_sport', '0011_games_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='url',
            field=models.SlugField(default=django.utils.timezone.now, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]
