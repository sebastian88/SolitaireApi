from rest_framework import serializers
from gameapi.models import Game, Card, Move, InitialPosition


class GameSerializer(serializers.Serializer):
    class meta:
        model = Game
        fields = ('id', 'Created')


class CardSerializer(serializers.Serializer):
    class meta:
        model = Card
        fields = ('name', 'codename')


class InitalPositionSerializer(serializers.Serializer):
    class meta:
        model = InitialPosition
        fields = ('game', 'shuffled_position', 'card')


class MoveSerializer(serializers.Serializer):
    class meta:
        model = Move
        fields = ('game', 'move_number', 'top_card', 'bottom_card')
