from django.contrib import admin

from .models import Game, GameDescription, Cart

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'price', 'language', 'players_min', 'players_max', 'playtime_min', 'playtime_max')
    search_fields = ('name', 'article', 'language')
    list_filter = ('language',)

class GameDescriptionAdmin(admin.ModelAdmin):
    list_display = ('game', 'description')

class CartAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'total_price')
    
admin.site.register(Game)
admin.site.register(GameDescription)
admin.site.register(Cart)