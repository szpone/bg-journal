from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    group = models.IntegerField(null=True, blank=True)
    confirm_password = models.CharField(max_length=128)


class BoardGame(models.Model):
    name = models.CharField(max_length=128)
    edition = models.IntegerField(null=True, blank=True)


class Expansion(models.Model):
    name = models.CharField(max_length=128)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, null=True, blank=True)


class Match(models.Model):
    victory = models.BooleanField(default=False)
    points = models.IntegerField(default=0, null=True, blank=True)
    scenario = models.CharField(max_length=128, null=True, blank=True)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    players = models.ManyToManyField('api.User', related_name='players')

    @property
    def board_game_name(self):
        return self.board_game.name
