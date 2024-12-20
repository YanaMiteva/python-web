from django.db import models
from django.db.models import Manager

from django102.models.player import Player

class GameManager(models.Manager):
    def all_with_players_count(self):
        return self.all()\
            .annotate(players_count=models.Count('players'))



class Game(models.Model):
    objects = GameManager()
    DIFFICULTY_LEVELS_CHOICES = (
        (0, 'Easy'),
        (1, 'Normal'),
        (2, 'Hard'),

    )
    name = models.CharField(max_length=30, blank=False)
    level_of_difficulty = models.IntegerField(
        blank=False,
        choices=DIFFICULTY_LEVELS_CHOICES
    )
    players = models.ManyToManyField(Player)

