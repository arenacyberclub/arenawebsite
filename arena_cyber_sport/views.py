
from django.views.generic.base import View
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Games, News, Tournaments, Banner, Product, Team, Member



# Create your views here.
class Index(View):
    def get(self, request):
        games=Games.objects.all()
        news=News.objects.all()
        banner=Banner.objects.all()
        context = {"games":games, "news":news, "banner":banner}
        return render(request, "arena_cyber_sport/index.html", context)        
class GamesView(View):
    def get(self, request):
        games = Games.objects.all()
        paginator = Paginator(games, per_page=2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "arena_cyber_sport/games_list.html", {"page_obj":page_obj})

class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        return render(request, "arena_cyber_sport/newspage.html", {"news":news})


class NewsDetailView(View):
    def get(self, request, slug):
        news = News.objects.get(url=slug)
        return render(request, "arena_cyber_sport/newsarticle.html", {"news":news})



class GameDetailView(View):
    def get(self, request, slug):
        game = Games.objects.get(url=slug)
        return render(request, "arena_cyber_sport/game_page.html", {"game":game})

class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "arena_cyber_sport/store-catalog.html", {"products":products})

class ProductPage(View):
    def get(self, request, slug):
        product = News.objects.get(url=slug)
        return render(request, "arena_cyber_sport/store-product.html", {"product":product})

class TournamentsView(View):
    def get(self, request):
        tournaments = Tournaments.objects.all()
        return render(request, 'arena_cyber_sport/tournaments.html', {"tournaments":tournaments})

class StoreView(View):
    def get(self, request):
        products = Product.objects.all()
        games = Games.objects.all()
        return render(request, "arena_cyber_sport/store.html", {"products":products,
        "games":games})
        

class TeamsView(View):
    def get(self, request):
        members = Member.objects.all()
        teams = Team.objects.all()
        return render(request, 'arena_cyber_sport/teams.html', {"teams":teams,
        "members":members})

class MemberView(View):
    def get(self, request, slug):
        member = Member.objects.get(url=slug)
        return render(request, "arena_cyber_sport/member.html", {"member":member})