from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255)
    article = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='game_images', null=True, blank=True)
    players_min = models.PositiveIntegerField(null=True, blank=True)
    players_max = models.PositiveIntegerField(null=True, blank=True)
    playtime_min = models.PositiveIntegerField(null=True, blank=True)
    playtime_max = models.PositiveIntegerField(null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
class GameDescription(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.game.name} - {self.description[:20]}"

class Cart(models.Model):
    games = models.ManyToManyField(Game, blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"Cart {self.pk}"