# Generated by Django 3.2.16 on 2023-01-19 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(max_length=300)),
                ('banner_text', models.TextField()),
                ('banner_pic', models.ImageField(upload_to='banner_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100)),
                ('game_desc', models.TextField()),
                ('rating', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GamesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('team_logo', models.ImageField(upload_to='teams/')),
            ],
        ),
        migrations.CreateModel(
            name='TourCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tournaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=100)),
                ('tour_time', models.DateField()),
                ('teams', models.ManyToManyField(to='arena_cyber_sport.Team')),
                ('tour_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena_cyber_sport.tourcategory')),
                ('tour_game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena_cyber_sport.games')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_desc', models.TextField()),
                ('first_price', models.SmallIntegerField()),
                ('selling_price', models.SmallIntegerField()),
                ('product_pic1', models.ImageField(upload_to='store/')),
                ('product_pic2', models.ImageField(blank=True, upload_to='store/')),
                ('product_pic3', models.ImageField(blank=True, upload_to='store/')),
                ('product_pic4', models.ImageField(blank=True, upload_to='store/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena_cyber_sport.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=300)),
                ('news_desc', models.TextField()),
                ('news_pic', models.ImageField(upload_to='news/')),
                ('posted_date', models.DateField()),
                ('news_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena_cyber_sport.newscategory')),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='game_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena_cyber_sport.gamescategory'),
        ),
    ]