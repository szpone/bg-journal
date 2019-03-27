from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'bio', 'confirm_password')

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        data.pop('confirm_password')
        return data

    def create(self, validated_data):
        user = User.objects.create(email=validated_data.get('email'),
                                   username=validated_data.get('username'))
        user.set_password(validated_data.get('password'))
        user.save()
        return


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class BoardGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardGame
        fields = ('id', 'name', 'edition', 'id')


class MatchSerializer(serializers.ModelSerializer):
    players_names = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Match
        fields = ('id', 'victory', 'points', 'scenario', 'players', 'players_names', 'board_game_name',
                  'board_game', 'expansion')

    def get_players_names(self, obj):
        names = []
        for player in obj.players.all():
            names.append(player.username)
        return names


class ExpansionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expansion
        fields = ('id', 'name', 'board_game_name', 'board_game')
