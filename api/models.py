from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    group = models.IntegerField(null=True, blank=True)
    # confirm_password = models.CharField(max_length=128)


class BoardGame(models.Model):
    name = models.CharField(max_length=128)
    edition = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Expansion(models.Model):
    name = models.CharField(max_length=128)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def board_game_name(self):
        return self.board_game.name


class Match(models.Model):
    victory = models.BooleanField(default=False)
    points = models.IntegerField(default=0, null=True, blank=True)
    scenario = models.CharField(max_length=128, null=True, blank=True)
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    players = models.ManyToManyField('api.User', related_name='players')
    expansion = models.ForeignKey(Expansion, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(editable=False)

    def board_game_name(self):
        return self.board_game.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)
