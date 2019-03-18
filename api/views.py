from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from .serializers import (UserSerializer, BoardGameSerializer, MatchSerializer, ExpansionSerializer)
from django.db.models import Count

User = get_user_model()

# Create your views here.


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardGameListView(ListAPIView):
    queryset = BoardGame.objects.select_related('expansion')
    serializer_class = BoardGameSerializer


class MatchListView(ListCreateAPIView):
    queryset = Match.objects.select_related('board_game', 'expansion').prefetch_related('players')
    serializer_class = MatchSerializer

    def get_queryset(self):
        qs = self.queryset
        user = self.request.user
        return qs.filter(players=user)


class ExpansionListView(ListAPIView):
    queryset = Expansion.objects.select_related('board_game')
    serializer_class = ExpansionSerializer


class TopThreeListView(ListAPIView):
    queryset = Match.objects.select_related('board_game').prefetch_related('players')
    serializer_class = MatchSerializer

    def get_queryset(self):
        qs = self.queryset
        user = self.request.user
        qs = qs.filter(players=user).values('board_game').annotate(ct=Count('board_game')).order_by('-ct')[:3]
        return qs
