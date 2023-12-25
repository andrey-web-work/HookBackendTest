from django.contrib.auth.models import User

from rest_framework.serializers import DecimalField, IntegerField, ModelSerializer

from .models import MoveModel, RoundModel


class MoveSerializer(ModelSerializer):
    class Meta:
        model = MoveModel
        fields = ["user", "round", "value", "jackpot"]
        read_only_fields = ["user", "round", "value", "jackpot"]


class UsersCountField(IntegerField):
    def to_representation(self, value):
        users = value.distinct("user").count()

        return super().to_representation(users)


class RoundStatsSerializer(ModelSerializer):
    users_count = UsersCountField(read_only=True, source="history")

    class Meta:
        model = RoundModel
        fields = ["id", "users_count"]


class RoundsCountField(IntegerField):
    def to_representation(self, value):
        rounds = value.distinct("round").count()

        return super().to_representation(rounds)


class AverageMovesField(DecimalField):
    def to_representation(self, value):
        moves = value.count()
        rounds = value.distinct("round").count()
        if rounds:
            average_moves = moves / rounds
        else:
            average_moves = 0

        return super().to_representation(average_moves)


class UserStatsSerializer(ModelSerializer):
    rounds_count = RoundsCountField(read_only=True, source="moves")
    average_moves = AverageMovesField(read_only=True, source="moves", max_digits=None, decimal_places=2)

    class Meta:
        model = User
        fields = ["id", "rounds_count", "average_moves"]
