# Generated by Django 3.2.16 on 2023-01-26 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arena_cyber_sport', '0013_auto_20230125_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='banner_text_en',
            new_name='banner_text_tm',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='banner_title_en',
            new_name='banner_title_tm',
        ),
        migrations.RenameField(
            model_name='games',
            old_name='game_desc_en',
            new_name='game_desc_tm',
        ),
        migrations.RenameField(
            model_name='games',
            old_name='game_name_en',
            new_name='game_name_tm',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='news_desc_en',
            new_name='news_desc_tm',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='news_title_en',
            new_name='news_title_tm',
        ),
    ]