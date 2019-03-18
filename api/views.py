from rest_framework.generics import ListAPIView, ListCreateAPIView, APIView
from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from .serializers import (UserSerializer, BoardGameSerializer, MatchSerializer, ExpansionSerializer,
                          DashboardSerializer)

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



