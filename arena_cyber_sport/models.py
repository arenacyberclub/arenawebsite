from django.db import models
from django.urls import reverse

# Create your models here.
#banner
class Banner(models.Model):
    banner_title = models.CharField(max_length=300)
    banner_text = models.TextField()
    banner_pic = models.ImageField(upload_to='banner_pic/')
    def __str__(self):
        return self.banner_title

#news_category
class NewsCategory(models.Model):
    news_category = models.CharField(max_length=30)
    def __str__(self):
        return self.news_category
#news1

class News(models.Model):
    news_title = models.CharField(max_length=300)
    news_desc = models.TextField()
    news_category = models.ForeignKey("NewsCategory", on_delete=models.CASCADE)
    news_pic = models.ImageField(upload_to='news/')
    posted_date = models.DateField()
    url = models.SlugField(max_length=130, unique=True)
    def __str__(self):
        return self.news_title
    
    def get_absolute_url(self):
        return reverse("newsdetail", kwargs={"slug":self.url})
    
#GamesCategory
class GamesCategory(models.Model):
    game_category = models.CharField(max_length=30)
    def __str__(self):
        return self.game_category
#Games
class Games(models.Model):
    game_name = models.CharField(max_length=100)
    game_category = models.ForeignKey('GamesCategory', on_delete=models.CASCADE)
    game_desc = models.TextField()
    rating = models.SmallIntegerField()
    game_pic = models.ImageField(upload_to="games/")
    url = models.SlugField(max_length=130, unique=True)
    def __str__(self):
        return self.game_name
    def get_absolute_url(self):
        return reverse("gamedetail", kwargs={"slug":self.url})

#Products
class ProductCategory(models.Model):
    product_category = models.CharField(max_length=50)
    def __str__(self):
        return self.product_category


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.ForeignKey("ProductCategory",on_delete= models.CASCADE)
    product_desc = models.TextField()
    first_price = models.SmallIntegerField()
    selling_price = models.SmallIntegerField()
    product_pic1 = models.ImageField(upload_to="store/")
    product_pic2 = models.ImageField(blank=True, upload_to="store/")
    product_pic3 = models.ImageField(blank=True, upload_to="store/")
    product_pic4 = models.ImageField(blank=True, upload_to="store/")

#Teams
class Team(models.Model):
    team_name=models.CharField(max_length=30)
    team_logo=models.ImageField(upload_to='teams/')
    def __str__(self):
        return self.team_name

#Tournaments
class TourCategory(models.Model):
    tour_category=models.CharField(max_length=50)
    def __str__(self):
        return self.tour_category

class Tournaments(models.Model):
    tour_game = models.ForeignKey("Games", on_delete=models.CASCADE)
    tour_name = models.CharField(max_length=100)
    tour_time = models.DateField()
    teams = models.ManyToManyField("Team")
    tour_category = models.ForeignKey("TourCategory", on_delete=models.CASCADE)
    def __str__(self):
        return self.tour_name

#Member
class Member(models.Model):
    member_level=[
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
        ]
    member_name = models.CharField(max_length=60)
    member_nick = models.CharField(max_length=10)
    member_team = models.ForeignKey(Team, on_delete = models.CASCADE)
    member_pic = models.ImageField(upload_to="member/")
    member_position = models.CharField(max_length=2, choices=member_level)
    url = models.SlugField(max_length=130, unique=True)                                                                                                               
    def __str__(self):
        return self.member_nick
    def get_absolute_url(self):
        return reverse("member", kwargs={"slug":self.url})