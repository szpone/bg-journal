from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView
from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from .serializers import (BoardGameSerializer, MatchSerializer, ExpansionSerializer,
                          UserCreateSerializer, UserListSerializer)
from django.db.models import Count

User = get_user_model()

# Create your views here.


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class BoardGameListView(ListAPIView):
    queryset = BoardGame.objects.all()
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
