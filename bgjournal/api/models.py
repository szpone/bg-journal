from django.db import models

# Create your models here.


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
    players = models.ManyToManyField('auth.User', related_name='players')




