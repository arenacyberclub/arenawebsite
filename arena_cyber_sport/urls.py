from django.urls import path

from . import views


urlpatterns = [
    path("", views.Index.as_view()),
    path("index", views.Index.as_view(), name="index"),
    path("news", views.NewsView.as_view(), name="news"),
    path("products", views.ProductView.as_view(), name="products"),
    path("product", views.ProductPage.as_view(), name ="productpage"),
    path("store", views.StoreView.as_view(), name="store"),
    path("games/", views.GamesView.as_view(), name="games"),
    path("teams", views.TeamsView.as_view(), name="teams"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="newsdetail"),
    path("games/<slug:slug>/", views.GameDetailView.as_view(), name="gamedetail"),
    path("member/<slug:slug>/", views.MemberView.as_view(), name="member"),
    path("tournaments", views.TournamentsView.as_view(), name="tournaments")

]
