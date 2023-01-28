from modeltranslation.translator import register, TranslationOptions
from .models import Games, News, Banner

@register(Games)
class GameTranslationOption(TranslationOptions):
    fields = ('game_name', 'game_desc')


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('news_title', 'news_desc')

@register(Banner)
class BannerTranslationOption(TranslationOptions):
    fields = ('banner_title', 'banner_text')