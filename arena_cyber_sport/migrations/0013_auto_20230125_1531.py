# Generated by Django 3.2.16 on 2023-01-25 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena_cyber_sport', '0012_member_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='banner_text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_title_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='banner',
            name='banner_title_ru',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='games',
            name='game_desc_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='games',
            name='game_desc_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='games',
            name='game_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='games',
            name='game_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_desc_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_desc_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_title_en',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='news_title_ru',
            field=models.CharField(max_length=300, null=True),
        ),
    ]