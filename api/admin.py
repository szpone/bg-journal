from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Match, BoardGame, Expansion

User = get_user_model()

# Register your models here.

admin.site.register(User)
admin.site.register(Match)
admin.site.register(BoardGame)
admin.site.register(Expansion)
