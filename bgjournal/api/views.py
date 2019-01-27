from rest_framework.generics import ListAPIView, ListCreateAPIView
from django.contrib.auth.models import User
from .models import BoardGame, Match, Expansion
from .serializers import UserSerializer, BoardGameSerializer, MatchSerializer, ExpansionSerializer
from rest_framework.response import Response

# Create your views here.


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BoardGameListView(ListAPIView):
    queryset = BoardGame.objects.all()
    serializer_class = BoardGameSerializer


class MatchListView(ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class ExpansionListView(ListAPIView):
    queryset = Expansion.objects.all()
    serializer_class = ExpansionSerializer









