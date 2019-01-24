from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User
from .models import BoardGame, Match
from .serializers import UserSerializer, BoardGameSerializer, MatchSerializer
# Create your views here.


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardGameListView(ListAPIView):
    queryset = BoardGame.objects.all()
    serializer_class = BoardGameSerializer


class MatchListView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class ExpansionListView(ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer









