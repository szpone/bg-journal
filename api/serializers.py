from django.contrib.auth import get_user_model
from .models import BoardGame, Match, Expansion
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'group', 'bio', 'confirm_password')

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match')
        data.pop('confirm_password')
        return data

    def create(self, validated_data):
        # user = super().create(validated_data)
        user = User.objects.create(email=validated_data.get('email'),
                                   username=validated_data.get('username'))
        user.set_password(validated_data['password'])
        user.save()
        return user


class BoardGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardGame
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('board_game', 'board_game_name', 'victory', 'points', 'scenario', 'players')


class ExpansionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expansion
        fields = '__all__'
