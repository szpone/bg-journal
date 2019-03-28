from rest_framework.generics import (ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView,
                                     RetrieveUpdateAPIView, UpdateAPIView)
from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from .serializers import (BoardGameSerializer, MatchSerializer, ExpansionSerializer,
                          UserCreateSerializer, UserListSerializer, UserChangePasswordSerializer, UserEditSerializer)
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.db.models import Count

User = get_user_model()

# Create your views here.


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserEditView(RetrieveUpdateAPIView):
    serializer_class = UserEditSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        if self.request.user.id == kwargs['pk'] or self.request.user.is_superuser:
            serializer = UserEditSerializer(self.request.user)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data)


class UserChangePasswordView(UpdateAPIView):
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self, queryset=None):
        return self.request.user


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


class MatchEditDeleteView(RetrieveUpdateDestroyAPIView):
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
