from django.contrib import admin
from .models import Match, BoardGame, Expansion

# Register your models here.


admin.site.register(Match)
admin.site.register(BoardGame)
admin.site.register(Expansion)
