from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from .serializers import (UserSerializer, BoardGameSerializer, MatchSerializer, ExpansionSerializer,
                          )
from django.db.models import Count

User = get_user_model()

# Create your views here.


class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardGameListView(ListAPIView):
    queryset = BoardGame.objects.all()
    serializer_class = BoardGameSerializer


class MatchListView(ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        return Match.objects.filter(players__id=request.user.id)


class ExpansionListView(ListAPIView):
    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer


class TopThreeListView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def list(self, request):
        qs = self.get_queryset()
        user = request.user
        return qs.filter(players=user).values('board_game').annotate(ct=Count('board_game')).order_by('-ct')[:3]



