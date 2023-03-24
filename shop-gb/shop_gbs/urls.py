""" defines URL patterns for shop_gbs"""
from django.urls import path
from .views import GameListView, GameDetailView, CartListView

urlpatterns = [
    # path('', views.index, name='index'),
    path('games/', GameListView.as_view(), name='game_list'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game_detail'),
    path('cart/', CartListView.as_view(), name='cart'),
]