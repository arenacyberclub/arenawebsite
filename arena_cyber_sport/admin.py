from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import GamesCategory, Games, News, NewsCategory, Team, TourCategory, Tournaments, Product, ProductCategory, Member, Banner


admin.site.register(GamesCategory),
admin.site.register(Games)
class GamePic(admin.ModelAdmin):
    list_display = ("id","get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.game_pic.url} width="50" height="60"/>')
admin.site.register(News),
admin.site.register(NewsCategory),
admin.site.register(Team),
admin.site.register(TourCategory),
admin.site.register(Tournaments),
admin.site.register(Product),
admin.site.register(ProductCategory),
admin.site.register(Member),
admin.site.register(Banner),